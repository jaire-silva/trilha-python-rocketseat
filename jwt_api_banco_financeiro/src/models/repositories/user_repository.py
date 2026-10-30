from sqlalchemy.orm import scoped_session

from jwt_api_banco_financeiro.src.models.entities.user_entity import UserEntity


class UserRepository:
    def __init__(self, session: scoped_session):
        self.__session = session

    def registry_user(self, username: str, password: str) -> None:
        user = UserEntity(username=username, password=password)
        self.__session.add(user)
        self.__session.commit()
