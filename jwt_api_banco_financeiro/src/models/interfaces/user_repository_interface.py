from abc import ABC, abstractmethod

from jwt_api_banco_financeiro.src.models.entities.user_entity import UserEntity


class UserRepositoryInterface(ABC):
    @abstractmethod
    def registry_user(self, username: str, password: str) -> UserEntity:
        pass

    @abstractmethod
    def edit_balance(self, user_id: int, new_balance: float) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> UserEntity | None:
        pass
