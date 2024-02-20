from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# Создание моделей
db = SQLAlchemy()


class User(db.Model):
    """Описание полей моделей"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    surname = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'Имя: {self.username},  Фамилия: {self.surname},  Почта: {self.email},  Пароль: {self.password})'
