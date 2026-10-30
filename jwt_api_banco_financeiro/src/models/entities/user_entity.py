from jwt_api_banco_financeiro.src.models.settings.db import db


class UserEntity(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Float, nullable=False, default=0.0)
