from fast_api_crud_de_usuario.src.models.repositories.interfaces.users_repository_interface import \
    UsersRepositoryInterface


class UserFinderController:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def find_user_by_id(self, user_id: int) -> dict:
        user = await self.__find_user(user_id)
        return self.__format_response(user)

    async def __find_user(self, user_id: int) -> dict:
        return await self.users_repository.get_user_by_id(user_id)

    def __format_response(self, user_data: dict) -> dict:
        return {
            'Type': 'USER',
            'Count': 1,
            'Attributes': user_data
        }
