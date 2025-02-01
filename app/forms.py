# app/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, FileField
from wtforms.validators import DataRequired

class TextToSpeechForm(FlaskForm):
    text = StringField('Enter Text:', validators=[DataRequired()])
    language = SelectField('Language:', choices=[('en-US', 'English'), ('hi-IN', 'Hindi'), ('te-IN', 'Telugu')])
    gender = SelectField('Gender:', choices=[('MALE', 'Male'), ('FEMALE', 'Female')])
    submit = SubmitField('Convert to Speech')

class SpeechToTextForm(FlaskForm):
    audio = FileField('Upload Audio:', validators=[DataRequired()])
    submit = SubmitField('Convert to Text')

class PdfToSpeechForm(FlaskForm):
    pdf = FileField('Upload PDF:', validators=[DataRequired()])
    submit = SubmitField('Convert PDF to Speech')

class PdfSummaryForm(FlaskForm):
    pdf = FileField('Upload PDF:', validators=[DataRequired()])
    submit = SubmitField('Summarize PDF')
