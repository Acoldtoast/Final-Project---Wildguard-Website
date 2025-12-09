# wildguard/routes/pages.py

from flask import Blueprint, render_template
from models import Organization, HelpTip, RelatedArticle, News

pages = Blueprint('pages', __name__)

@pages.route("/")
def home():
    return render_template('home.html', title='Home')

@pages.route("/about")
def about():
    return render_template('about.html', title='Our Commitment')

@pages.route("/sources")
def sources():
    return render_template('sources.html', title='Sources & References')

@pages.route("/help")
def help_page():
    help_tips = HelpTip.query.all()
    return render_template('help.html', title='How to Help', help_tips=help_tips)

@pages.route("/donate")
def donate():
    organizations = Organization.query.all()
    return render_template('donate.html', title='Organizations', organizations=organizations)

@pages.route("/articles")
def articles():
    all_articles = RelatedArticle.query.order_by(RelatedArticle.id).all()
    return render_template('articles.html', title='Resources & Articles', articles=all_articles)

@pages.route("/news")
def news():
    news_items = News.query.order_by(News.published_date.desc()).all()
    return render_template('news.html', title='News & Updates', news_items=news_items)


