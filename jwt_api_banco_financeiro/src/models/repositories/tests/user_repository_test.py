from flask import Flask

from jwt_api_banco_financeiro.src.models.repositories.user_repository import UserRepository
from jwt_api_banco_financeiro.src.models.settings.db_connection_handler import DBConnectionHandler


def test_registry_user():
    app = Flask(__name__)
    db_connection_handler = DBConnectionHandler()
    db_connection_handler.init_app(app)

    with app.app_context():
        session_ativa = db_connection_handler.get_session()
        UserRepository(session_ativa)
