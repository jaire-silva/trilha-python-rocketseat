from fast_api_crud_de_usuario.src.models.repositories.interfaces.users_repository_interface import \
    UsersRepositoryInterface


class UserRegisterController:
    def __init__(self, users_repository: UsersRepositoryInterface):
        self.users_repository = users_repository

    async def register_user(self, user_data: dict) -> dict:
        self.__validate_user_data(user_data)
        await self.__registry_user(user_data)
        return self.__format_response(user_data)

    def __validate_user_data(self, user_data: dict) -> bool:
        age = user_data.get('age')
        uf = user_data.get('uf')

        if uf not in ['MG', 'BA', 'CE', 'SC', 'MT']:
            raise Exception('Estado inválido para cadastro')

        if age < 0 or age > 120:
            raise Exception('Idade inválida para cadastro')

    async def __registry_user(self, user_data: dict) -> None:
        await self.users_repository.insert_user(user_data)

    def __format_response(self, user_data: dict) -> dict:
        return {
            'Type': 'USER',
            'Count': 1,
            'Attributes': user_data
        }
