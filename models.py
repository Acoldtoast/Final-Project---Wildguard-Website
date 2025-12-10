# wildguard/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

# --- NORMALIZED DATABASE TABLES ---

class ConservationStatus(db.Model):
    __tablename__ = 'conservation_status'
    status_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status_name = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text, nullable=False)
    species = db.relationship('Species', backref='status', lazy=True)

class Location(db.Model):
    __tablename__ = 'location'
    location_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    location_name = db.Column(db.String(100), nullable=False, unique=True)

class HabitatType(db.Model):
    __tablename__ = 'habitat_type'
    habitat_type_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    habitat_name = db.Column(db.String(100), nullable=False, unique=True)

class SpeciesHabitat(db.Model):
    __tablename__ = 'species_habitat'
    habitat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.location_id', ondelete='CASCADE'), nullable=False)
    habitat_type_id = db.Column(db.Integer, db.ForeignKey('habitat_type.habitat_type_id', ondelete='CASCADE'), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('species_id', 'location_id', 'habitat_type_id'),
    )

class Threat(db.Model):
    __tablename__ = 'threat'
    threat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    threat_name = db.Column(db.String(150), nullable=False, unique=True)

class SpeciesThreat(db.Model):
    __tablename__ = 'species_threats'
    species_threat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    threat_id = db.Column(db.Integer, db.ForeignKey('threat.threat_id', ondelete='CASCADE'), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('species_id', 'threat_id'),
    )

class SpeciesFunFact(db.Model):
    __tablename__ = 'species_funfacts'
    fact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    fact_detail = db.Column(db.Text, nullable=False)

class OrganizationSupports(db.Model):
    __tablename__ = 'organization_supports'
    ogs_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_id = db.Column(db.Integer, db.ForeignKey('organization.org_id', ondelete='CASCADE'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    support_type = db.Column(db.String(100), nullable=False)
    
    __table_args__ = (
        db.UniqueConstraint('org_id', 'species_id', 'support_type'),
    )

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True, index=True)
    scientific_name = db.Column(db.String(100), nullable=False)
    population_estimate = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), default='default_species.jpg')
    status_id = db.Column(db.Integer, db.ForeignKey('conservation_status.status_id'), nullable=False)

    habitats = db.relationship('SpeciesHabitat', backref='species', cascade="all, delete-orphan", lazy='dynamic')
    threats = db.relationship('SpeciesThreat', backref='species', cascade="all, delete-orphan", lazy='dynamic')
    fun_facts = db.relationship('SpeciesFunFact', backref='species', cascade="all, delete-orphan", lazy='dynamic')
    supported_by = db.relationship('Organization', secondary='organization_supports', backref='supported_species')

class Organization(db.Model):
    __tablename__ = 'organization'
    org_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False, unique=True)
    about = db.Column(db.Text, nullable=False)
    website = db.Column(db.String(200), nullable=False)
    donate_link = db.Column(db.String(200))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class HelpTip(db.Model):
    __tablename__ = 'help_tip'
    help_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.Text, nullable=False)

class HelpTipAction(db.Model):
    __tablename__ = 'help_tip_action'
    action_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tip_id = db.Column(db.Integer, db.ForeignKey('help_tip.help_id', ondelete='CASCADE'), nullable=False)
    action_text = db.Column(db.Text, nullable=False)
    
    tip = db.relationship('HelpTip', backref=db.backref('actions', cascade="all, delete-orphan", lazy='dynamic'))

class RelatedArticle(db.Model):
    __tablename__ = 'related_article'
    article_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')

class News(db.Model):
    __tablename__ = 'news'
    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')
    published_date = db.Column(db.Date, nullable=True)