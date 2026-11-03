from drivers.password_handler import PasswordHandler
from jwt_api_banco_financeiro.src.models.entities.user_entity import UserEntity
from jwt_api_banco_financeiro.src.models.interfaces.user_repository_interface import UserRepositoryInterface


class UserController:
    def __init__(self, user_repository: UserRepositoryInterface):
        self.__user_repository = user_repository
        self.__password_handler = PasswordHandler()

    def registry_user(self, username: str, password: str) -> dict:
        hashed_password = self.__create_hash_password(password)
        new_user = self.__registry_new_user(username, hashed_password)
        response = self.__format_response(new_user)
        return response

    def __create_hash_password(self, password: str) -> str:
        hashed_password = self.__password_handler.encrypt_password(password)
        return str(hashed_password)

    def __registry_new_user(self, username: str, hashed_password: str) -> UserEntity:
        return self.__user_repository.registry_user(username, hashed_password)

    def __format_response(self, user: UserEntity) -> dict:
        return {
            "type": "User",
            "count": 1,
            "attributes": {
                "id": user.id,
                "username": user.username,
                "balance": user.balance
            }
        }
