# pylint: disable=invalid-name

from flask import Flask
from sqlalchemy.orm import scoped_session

from jwt_api_banco_financeiro.src.models.settings.db import db


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "postgresql+psycopg2://admin:admin123@localhost:5432/jwt_api_banco_financeiro"

    def init_app(self, app: Flask) -> None:
        app.config["SQLALCHEMY_DATABASE_URI"] = self.__connection_string
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SECRET_KEY"] = "admin123"
        app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
            "pool_size": 5,
            "max_overflow": 10,
            "pool_pre_ping": True
        }

        db.init_app(app)

        with app.app_context():
            db.create_all()

    def get_session(self) -> scoped_session:
        return db.session
