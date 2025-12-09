# wildguard/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
db = SQLAlchemy()

class ConservationStatus(db.Model):
    __tablename__ = 'conservation_status'
    status_name = db.Column(db.String(50), primary_key=True)
    description = db.Column(db.Text, nullable=False)
    species = db.relationship('Species', backref='status', lazy=True)

class SpeciesHabitat(db.Model):
    __tablename__ = 'species_habitat'
    habitat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    habitat_location = db.Column(db.String(250), nullable=False)

    __table_args__ = (
        db.UniqueConstraint('species_id', 'habitat_location'), 
    )

class SpeciesThreat(db.Model):
    __tablename__ = 'species_threats'
    threat_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    threat_name = db.Column(db.String(150), nullable=False)
    __table_args__ = (
        db.UniqueConstraint('species_id', 'threat_name'),
    )

class SpeciesFunFact(db.Model):
    __tablename__ = 'species_funfacts'
    fact_id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # NEW PK
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    fact_detail = db.Column(db.Text, nullable=False)

class OrganizationSupports(db.Model):
    __tablename__ = 'organization_supports'
    ogs_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    org_id = db.Column(db.Integer, db.ForeignKey('organization.org_id', ondelete='CASCADE'), nullable=False)
    species_id = db.Column(db.Integer, db.ForeignKey('species.id', ondelete='CASCADE'), nullable=False)
    support_type = db.Column(db.String(100), nullable=False)
    __table_args__ = (db.UniqueConstraint('org_id', 'species_id', 'support_type'),)

class Species(db.Model):
    __tablename__ = 'species'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True, index=True)
    scientific_name = db.Column(db.String(100), nullable=False)
    population_estimate = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), default='default_species.jpg')
    status_name = db.Column(db.String(50), db.ForeignKey('conservation_status.status_name'), nullable=False)

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
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class HelpTip(db.Model):
    __tablename__ = 'help_tip'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    reason = db.Column(db.Text, nullable=False)
    action = db.Column(db.Text, nullable=False)

class RelatedArticle(db.Model):
    __tablename__ = 'related_article'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')  # e.g., 'General', 'Scientific', 'Policy'

class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    summary = db.Column(db.Text, nullable=False)
    link = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False, default='General')  # e.g., 'Success Story', 'Alert', 'Update'
    published_date = db.Column(db.Date, nullable=True)
