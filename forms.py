from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class RegistrationForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired(), Length(min=2, max=150)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

class AccessForm(FlaskForm):
    group_id = SelectField('Группа', coerce=int)
    file_id = SelectField('Файл', coerce=int)
    submit = SubmitField('Предоставить доступ')

class FolderForm(FlaskForm):
    name = StringField('Имя папки', validators=[DataRequired()])
    submit = SubmitField('Создать папку')

class FAQForm(FlaskForm):
    question = StringField('Вопрос', validators=[DataRequired()])
    answer = TextAreaField('Ответ', validators=[DataRequired()])
    submit = SubmitField('Добавить FAQ')
