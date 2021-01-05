from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileRequired
from wtforms import StringField, FileField, MultipleFileField, SelectField, TextAreaField, FieldList, FormField
from wtforms.validators import DataRequired

class RegistrationChef(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    avatar = FileField('avatar')

class IngredientRecipe(FlaskForm):
    name = StringField('name')
    
class RegistrationRecipe(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    ingredients = FieldList(StringField('ingredients[]', validators=[DataRequired()]))
    preparation = StringField('preparation[]')
    adicional_information = TextAreaField('adicional_information')
    recipe_img = MultipleFileField('recipe_img')
    