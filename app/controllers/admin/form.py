from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField
from wtforms.validators import DataRequired

class RegistrationChef(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    avatar = FileField('avatar')