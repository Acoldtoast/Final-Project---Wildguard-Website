# wildguard/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Optional, URL

# --- Authentication Forms ---

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# --- Species Management Form ---

class SpeciesForm(FlaskForm):
    name = StringField('Species Name', 
                       validators=[DataRequired(), Length(max=100)])
    scientific_name = StringField('Scientific Name', 
                                  validators=[DataRequired(), Length(max=100)])
    status = SelectField('Conservation Status', 
                         validators=[DataRequired()])
    population_estimate = StringField('Population Estimate', 
                                      validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', 
                               validators=[DataRequired(), Length(min=50, max=5000)])
    image_file = StringField('Image Filename', 
                             validators=[Length(max=100)])
    habitats = TextAreaField('Habitats (one per line)', 
                             validators=[Optional(), Length(max=2000)])
    threats = TextAreaField('Threats (one per line)', 
                            validators=[Optional(), Length(max=2000)])
    fun_facts = TextAreaField('Fun Facts (one per line)', 
                              validators=[Optional(), Length(max=5000)])
    submit = SubmitField('Save Species')

# --- Related Article Form ---

class RelatedArticleForm(FlaskForm):
    title = StringField('Article Title', 
                       validators=[DataRequired(), Length(max=300)])
    description = TextAreaField('Description', 
                               validators=[DataRequired(), Length(min=20, max=1000)])
    link = StringField('Article URL', 
                      validators=[DataRequired(), URL()])
    category = SelectField('Category', 
                          choices=[('General', 'General'), ('Scientific', 'Scientific'), ('Policy', 'Policy')],
                          validators=[DataRequired()])
    submit = SubmitField('Save Article')

# --- News Form ---

class NewsForm(FlaskForm):
    title = StringField('News Title', 
                       validators=[DataRequired(), Length(max=300)])
    summary = TextAreaField('Summary', 
                           validators=[DataRequired(), Length(min=20, max=1000)])
    link = StringField('News URL', 
                      validators=[DataRequired(), URL()])
    category = SelectField('Category', 
                          choices=[('Success Story', 'Success Story'), ('Alert', 'Alert'), ('Update', 'Update')],
                          validators=[DataRequired()])
    published_date = DateField('Published Date', validators=[Optional()])
    submit = SubmitField('Save News')
