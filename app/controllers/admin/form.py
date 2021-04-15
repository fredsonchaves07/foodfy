from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, MultipleFileField, SelectField, TextAreaField, FieldList, FormField, BooleanField
from wtforms.validators import DataRequired

class RegistrationChef(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    avatar = FileField('avatar')

    
class RegistrationRecipe(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    chef = SelectField('chef', choices=[("", "Selecione um chef")], validators=[DataRequired()])
    ingredients = FieldList(StringField('ingredients[]', validators=[DataRequired()]))
    preparations = FieldList(StringField('preparations[]', validators=[DataRequired()]))
    adicional_information = TextAreaField('adicional_information')
    recipe_img = MultipleFileField('recipe_img')
    
    
class RegistrationUser(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField('name', validators=[DataRequired()])
    admin = BooleanField('admin')
    