from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError, BooleanField
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired
from my_asset_project.models import MasterDropdown, User_Details
from flask import session


from flask_login import current_user
from my_asset_project.models import User


class LoginForm(FlaskForm):
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    AIC_office = StringField("AIC Office", validators=[DataRequired()])
    domain_name = SelectField("domain_name", validators=[DataRequired()])
    user_email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm', message='Password must match!')])
    pass_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def set_choices(self):
        # Fetch choices from the database for AIC_office
        self.domain_name.choices = [(str(user.domain_name), user.domain_name) for user in User_Details.query.all()]

        self.domain_name.choices.insert(0, ("", "Select a Domain Name"))

    def populate_obj(self, obj):
        super().populate_obj(obj)
        # Convert the selected user_name back to their names
        obj.domain_name = self.domain_name.data

    def check_user_email(self, field):
        if User.query.filter_by(user_email = field.data).first():
            raise ValidationError("Your email has been registered already!")
    

    def check_user_name(self, field):
        if User.query.filter_by(domain_name = field.data).first():
            raise ValidationError("Your username has been registered already!")
        
    
