from flask import Flask

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_database(app: Flask) -> None:
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin123@localhost:5432/mvc_projeto_pet"
    app.config["SECRET_KEY"] = "admin123"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
