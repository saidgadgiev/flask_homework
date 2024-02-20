from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length


class RegistrationForm(FlaskForm):
    """Форма регистрации"""
    username = StringField('Имя:', validators=[DataRequired()])
    surname = StringField('Фамилия:', validators=[DataRequired()])
    email = StringField('Email:', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль:', validators=[DataRequired(), Length(min=4)])
