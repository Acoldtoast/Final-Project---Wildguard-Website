# wildguard/routes/admin.py

from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from models import db, Species, SpeciesHabitat, SpeciesThreat, SpeciesFunFact, ConservationStatus, Organization, HelpTip, RelatedArticle, News
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
    help_tips = HelpTip.query.order_by(HelpTip.id).all()
    articles = RelatedArticle.query.order_by(RelatedArticle.id).all()
    news_items = News.query.order_by(News.published_date.desc()).all()
    return render_template("admin_dashboard.html", 
                         species_list=species_list,
                         organizations=organizations,
                         help_tips=help_tips,
                         articles=articles,
                         news_items=news_items)
    
def update_list(table, species_id, items, column, max_length=None):
    table.query.filter_by(species_id=species_id).delete()
    if items:
        for item in items.splitlines():
            item = item.strip()
            if (not max_length) or len(item) <= max_length:
                kwargs = { "species_id": species_id, column: item }
                db.session.add(table(**kwargs))


@admin.route("/admin/species", methods=["GET", "POST"])
@admin.route("/admin/species/<int:id>", methods=["GET", "POST"])
@admin_required
def manage_species(id=None):

    species = Species.query.get(id) if id else None
    
    if request.method == "GET" and species:
        habitats_text = "\n".join([h.habitat_location for h in species.habitats.all()])
        threats_text = "\n".join([t.threat_name for t in species.threats.all()])
        facts_text = "\n".join([f.fact_detail for f in species.fun_facts.order_by('fact_id').all()])
        form = SpeciesForm(obj=species)
        form.habitats.data = habitats_text
        form.threats.data = threats_text
        form.fun_facts.data = facts_text
    else:
        form = SpeciesForm(obj=species)

    form.status.choices = [(s.status_name, s.status_name) for s in ConservationStatus.query.all()]

    if form.validate_on_submit():
        if not species:
            species = Species()
            db.session.add(species)

        species.name = form.name.data
        species.scientific_name = form.scientific_name.data
        species.status_name = form.status.data
        species.population_estimate = form.population_estimate.data
        species.description = form.description.data
        species.image_file = form.image_file.data

        db.session.flush()
        update_list(SpeciesHabitat, species.id, form.habitats.data, "habitat_location", 250)
        update_list(SpeciesThreat, species.id, form.threats.data, "threat_name", 150)
        update_list(SpeciesFunFact, species.id, form.fun_facts.data, "fact_detail")

        db.session.commit()
        flash("Saved successfully.", "success")
        return redirect(url_for("admin.dashboard"))

    return render_template("admin_edit.html", form=form, species=species)


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
    help_tips = HelpTip.query.order_by(HelpTip.id).all()
    return render_template("admin_help_tips.html", help_tips=help_tips)


@admin.route("/admin/help-tip", methods=["GET", "POST"])
@admin.route("/admin/help-tip/<int:id>", methods=["GET", "POST"])
@admin_required
def edit_help_tip(id=None):
    tip = HelpTip.query.get(id) if id else None
    
    if request.method == "POST":
        title = request.form.get('title')
        reason = request.form.get('reason')
        action = request.form.get('action')
        
        if not title or not reason or not action:
            flash("Please fill in all required fields.", "danger")
            return redirect(url_for("admin.manage_help_tips"))
        
        if not tip:
            tip = HelpTip(title=title, reason=reason, action=action)
            db.session.add(tip)
        else:
            tip.title = title
            tip.reason = reason
            tip.action = action
        
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
    articles = RelatedArticle.query.order_by(RelatedArticle.id).all()
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
    news_items = News.query.order_by(News.id.desc()).all()
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
