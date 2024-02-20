# Задание №8
# 📌 Создать форму для регистрации пользователей на сайте.
# 📌 Форма должна содержать поля "Имя", "Фамилия", "Email",
# "Пароль" и кнопку "Зарегистрироваться".
# 📌 При отправке формы данные должны сохраняться в базе
# данных, а пароль должен быть зашифрован.

from models import db, User
from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from forms import RegistrationForm
import hashlib
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db.init_app(app)
app.config['SECRET_KEY'] = b'9b15f576d3fe61bd4b0dffd9230689db54cdbe38de825044d52a966eeee75d7f'
csrf = CSRFProtect(app)


@app.route('/')
def index():
    return redirect(url_for('register'))


@app.cli.command("init-db")
def init_db():
    """Создание таблиц в базе данных"""
    db.create_all()
    print('Все таблицы созданы успешно !')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    """Вьюшка регистрации с валидацией + сохранение в БД(с шифрованием пароля)"""
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        # Обработка данных из формы
        name = form.username.data
        surname = form.surname.data
        email = form.email.data
        password = form.password.data
        print(name, surname, email, password)
        salt = os.urandom(32)
        password_protection = password
        key = hashlib.pbkdf2_hmac('sha256', password_protection.encode('utf-8'), salt, 100000, dklen=128)
        user = User(username=name, surname=surname, email=email, password=key)
        print(user)
        db.session.add(user)
        db.session.commit()
        return f'<h2>Пользователь под именем: {name} добавлен в базу !</h2>' \
               f'<h3> Пароль зашифрован !<br> Экземпляр:<br>{user}</h3><br>(пароль - BLOB массив двоичных данных)'
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
