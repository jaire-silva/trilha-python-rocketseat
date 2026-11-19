from abc import ABC, abstractclassmethod


class UsersRepositoryInterface(ABC):

    @abstractclassmethod
    async def insert_user(self, user_info: dict):
        pass

    @abstractclassmethod
    async def get_user_by_id(self, user_id: int):
        pass
