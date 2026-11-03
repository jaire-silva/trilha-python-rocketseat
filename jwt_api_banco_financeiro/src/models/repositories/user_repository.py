from sqlalchemy.orm import scoped_session

from jwt_api_banco_financeiro.src.models.entities.user_entity import UserEntity
from jwt_api_banco_financeiro.src.models.interfaces.user_repository_interface import UserRepositoryInterface


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: scoped_session):
        self.__session = session

    def registry_user(self, username: str, password: str) -> UserEntity:
        user = UserEntity(username=username, password=password)
        self.__session.add(user)
        self.__session.commit()

        self.__session.refresh(user)

        return user

    def edit_balance(self, user_id: int, new_balance: float) -> None:
        user = self.__session.query(UserEntity).filter_by(id=user_id).first()
        user.balance = new_balance
        self.__session.commit()

    def get_user_by_id(self, user_id: int) -> UserEntity | None:
        return self.__session.query(UserEntity).filter_by(id=user_id).first()
