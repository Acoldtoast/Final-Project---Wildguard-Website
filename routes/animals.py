# wildguard/routes/admin.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import (db, Species, SpeciesHabitat, SpeciesThreat, SpeciesFunFact,
                    ConservationStatus, Organization, HelpTip, HelpTipAction,
                    RelatedArticle, News, Location, HabitatType, Threat, OrganizationSupports)
from forms import SpeciesForm, RelatedArticleForm, NewsForm
from functools import wraps

admin = Blueprint('admin', __name__)

def admin_required(f):
    @wraps(f)
    @login_required
    def wrapper(*args, **kwargs):
        if not current_user.is_admin:
            flash("Admin access only.", "danger")
            return redirect(url_for('pages.home'))
        return f(*args, **kwargs)
    return wrapper

@admin.route("/admin/dashboard")
@admin_required
def dashboard():
    species_list = Species.query.order_by(Species.id).all()
    organizations = Organization.query.order_by(Organization.org_id).all()
    help_tips = HelpTip.query.order_by(HelpTip.__table__.c.help_id).all()
    articles = RelatedArticle.query.order_by(RelatedArticle.__table__.c.article_id).all()
    news_items = News.query.order_by(News.published_date.desc()).all()
    return render_template("admin_dashboard.html", 
                         species_list=species_list,
                         organizations=organizations,
                         help_tips=help_tips,
                         articles=articles,
                         news_items=news_items)
    
def update_list(table, species_id, items, column, max_length=None):
    # Remove existing entries for species
    table.query.filter_by(species_id=species_id).delete()
    if not items:
        return

    for item in items.splitlines():
        item = item.strip()
        if not item:
            continue

        # SpeciesHabitat expects a "Location | HabitatType" format (or "Location - HabitatType").
        if table is SpeciesHabitat:
            if '|' in item:
                loc_name, hab_name = [p.strip() for p in item.split('|', 1)]
            elif '-' in item:
                loc_name, hab_name = [p.strip() for p in item.split('-', 1)]
            elif ':' in item:
                loc_name, hab_name = [p.strip() for p in item.split(':', 1)]
            else:
                loc_name = item
                hab_name = 'General'

            loc = Location.query.filter_by(location_name=loc_name).first()
            if not loc:
                loc = Location(location_name=loc_name)
                db.session.add(loc)
                db.session.flush()

            hab = HabitatType.query.filter_by(habitat_name=hab_name).first()
            if not hab:
                hab = HabitatType(habitat_name=hab_name)
                db.session.add(hab)
                db.session.flush()

            db.session.add(SpeciesHabitat(species_id=species_id, location_id=loc.location_id, habitat_type_id=hab.habitat_type_id))

        # SpeciesThreat expects plain threat names (one per line)
        elif table is SpeciesThreat:
            threat = Threat.query.filter_by(threat_name=item).first()
            if not threat:
                threat = Threat(threat_name=item)
                db.session.add(threat)
                db.session.flush()
            db.session.add(SpeciesThreat(species_id=species_id, threat_id=threat.threat_id))

        # Default handling (SpeciesFunFact etc.)
        else:
            if (not max_length) or len(item) <= max_length:
                kwargs = {"species_id": species_id, column: item}
                db.session.add(table(**kwargs))


@admin.route("/admin/species", methods=["GET", "POST"])
@admin.route("/admin/species/<int:id>", methods=["GET", "POST"])
@admin_required
def manage_species(id=None):

    species = Species.query.get(id) if id else None
    
    status_choices = [(s.status_name, s.status_name) for s in ConservationStatus.query.all()]
    
    if request.method == "GET" and species:
        habitats_text = "\n".join([
            f"{(Location.query.get(h.location_id).location_name if Location.query.get(h.location_id) else '')} | {(HabitatType.query.get(h.habitat_type_id).habitat_name if HabitatType.query.get(h.habitat_type_id) else '')}"
            for h in species.habitats.all()
        ])
        threats_text = "\n".join([
            (Threat.query.get(t.threat_id).threat_name if Threat.query.get(t.threat_id) else '')
            for t in species.threats.all()
        ])
        facts_text = "\n".join([f.fact_detail for f in species.fun_facts.order_by(SpeciesFunFact.fact_id).all()])
        form = SpeciesForm(obj=species)
        form.habitats.data = habitats_text
        form.threats.data = threats_text
        form.fun_facts.data = facts_text
    else:
        form = SpeciesForm(obj=species)

    form.status.choices = status_choices

    if form.validate_on_submit():

        is_new = False
        if not species:
            species = Species()
            is_new = True

        species.name = form.name.data
        species.scientific_name = form.scientific_name.data
        status = ConservationStatus.query.filter_by(status_name=form.status.data).first()
        if status:
            species.status_id = status.status_id
        species.population_estimate = form.population_estimate.data
        species.description = form.description.data
        species.image_file = form.image_file.data

        if is_new:
            db.session.add(species)

        db.session.flush()
        update_list(SpeciesHabitat, species.id, form.habitats.data, "habitat_location", 250)
        update_list(SpeciesThreat, species.id, form.threats.data, "threat_name", 150)
        update_list(SpeciesFunFact, species.id, form.fun_facts.data, "fact_detail")

        db.session.commit()
        flash("Saved successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin_edit.html", form=form, species=species, item_type="Species")


@admin.route("/admin/delete/<int:id>", methods=["POST"])
@admin_required
def delete_species(id):
    species = Species.query.get_or_404(id)
    db.session.delete(species)
    db.session.commit()
    flash("Species deleted.", "info")
    return redirect(url_for("admin.dashboard"))


# --- ORGANIZATIONS MANAGEMENT ---

@admin.route("/admin/organizations")
@admin_required
def manage_organizations():
    organizations = Organization.query.order_by(Organization.org_id).all()
    return render_template("admin_organizations.html", organizations=organizations)


@admin.route("/admin/organization", methods=["GET", "POST"])
@admin.route("/admin/organization/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_organization(id=None):
    org = Organization.query.get(id) if id else None
    
    if request.method == "POST":
        name = request.form.get('name')
        about = request.form.get('about')
        website = request.form.get('website')
        donate_link = request.form.get('donate_link')
        
        if not name or not about or not website:
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for("admin.manage_organizations"))
        
        if not org:
            org = Organization(name=name, about=about, website=website, donate_link=donate_link)
            db.session.add(org)
        else:
            org.name = name
            org.about = about
            org.website = website
            org.donate_link = donate_link
        
        db.session.commit()
        flash("Organization saved successfully.", "success")
        return redirect(url_for("admin.manage_organizations"))
    
    return render_template("admin_edit.html", item=org, item_type="Organization")


@admin.route("/admin/organization/delete/<int:id>", methods=["POST"])
@admin_required
def delete_organization(id):
    org = Organization.query.get_or_404(id)
    db.session.delete(org)
    db.session.commit()
    flash("Organization deleted.", "info")
    return redirect(url_for("admin.manage_organizations"))


# --- HELP TIPS MANAGEMENT ---

@admin.route("/admin/help-tips")
@admin_required
def manage_help_tips():
    help_tips = HelpTip.query.order_by(HelpTip.__table__.c.help_id).all()
    return render_template("admin_help_tips.html", help_tips=help_tips)


@admin.route("/admin/help-tip", methods=["GET", "POST"])
@admin.route("/admin/help-tip/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_help_tip(id=None):
    tip = HelpTip.query.get(id) if id else None
    if request.method == "GET" and tip:
        actions_text = "\n".join([a.action_text for a in tip.actions.order_by(HelpTipAction.action_id).all()])
        tip.action = actions_text

    if request.method == "POST":
        title = request.form.get('title')
        reason = request.form.get('reason')
        actions_raw = request.form.get('action')

        if not title or not reason or not actions_raw:
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for("admin.manage_help_tips"))

        if not tip:
            tip = HelpTip(title=title, reason=reason)
            db.session.add(tip)
            db.session.commit()  
        else:
            tip.title = title
            tip.reason = reason
            db.session.add(tip)
            db.session.commit()

        HelpTipAction.query.filter_by(tip_id=tip.help_id).delete()
        for line in actions_raw.splitlines():
            text = line.strip()
            if not text:
                continue
            if text.startswith('* '):
                text = text[2:].strip()
            if text:
                db.session.add(HelpTipAction(tip_id=tip.help_id, action_text=text))

        db.session.commit()
        flash("Help tip saved successfully.", "success")
        return redirect(url_for("admin.manage_help_tips"))

    return render_template("admin_edit.html", item=tip, item_type="Help Tip")


@admin.route("/admin/help-tip/delete/<int:id>", methods=["POST"])
@admin_required
def delete_help_tip(id):
    tip = HelpTip.query.get_or_404(id)
    db.session.delete(tip)
    db.session.commit()
    flash("Help tip deleted.", "info")
    return redirect(url_for("admin.manage_help_tips"))


# --- RELATED ARTICLES MANAGEMENT ---

@admin.route("/admin/articles")
@admin_required
def manage_articles():
    articles = RelatedArticle.query.order_by(RelatedArticle.__table__.c.article_id).all()
    return render_template("admin_articles.html", articles=articles)


@admin.route("/admin/article", methods=["GET", "POST"])
@admin.route("/admin/article/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_article(id=None):
    article = RelatedArticle.query.get(id) if id else None
    form = RelatedArticleForm(obj=article)
    
    if form.validate_on_submit():
        if not article:
            article = RelatedArticle()
            db.session.add(article)
        
        article.title = form.title.data
        article.description = form.description.data
        article.link = form.link.data
        article.category = form.category.data
        
        db.session.commit()
        flash("Article saved successfully.", "success")
        return redirect(url_for("admin.manage_articles"))
    
    return render_template("admin_edit.html", form=form, article=article, item_type="Related Article")


@admin.route("/admin/article/delete/<int:id>", methods=["POST"])
@admin_required
def delete_article(id):
    article = RelatedArticle.query.get_or_404(id)
    db.session.delete(article)
    db.session.commit()
    flash("Article deleted.", "info")
    return redirect(url_for("admin.manage_articles"))


# --- NEWS MANAGEMENT ---

@admin.route("/admin/news")
@admin_required
def manage_news():
    news_items = News.query.order_by(News.published_date.desc()).all()
    return render_template("admin_news.html", news_items=news_items)


@admin.route("/admin/news-item", methods=["GET", "POST"])
@admin.route("/admin/news-item/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_news(id=None):
    news_item = News.query.get(id) if id else None
    form = NewsForm(obj=news_item)
    
    if form.validate_on_submit():
        if not news_item:
            news_item = News()
            db.session.add(news_item)
        
        news_item.title = form.title.data
        news_item.summary = form.summary.data
        news_item.link = form.link.data
        news_item.category = form.category.data
        news_item.published_date = form.published_date.data
        
        db.session.commit()
        flash("News saved successfully.", "success")
        return redirect(url_for("admin.manage_news"))
    
    return render_template("admin_edit.html", form=form, news_item=news_item, item_type="News")


@admin.route("/admin/news-item/delete/<int:id>", methods=["POST"])
@admin_required
def delete_news(id):
    news_item = News.query.get_or_404(id)
    db.session.delete(news_item)
    db.session.commit()
    flash("News deleted.", "info")
    return redirect(url_for("admin.manage_news"))
