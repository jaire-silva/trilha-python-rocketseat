import pytest

from fast_api_crud_de_usuario.src.models.repositories.users_repository import UsersRepository


@pytest.mark.asyncio
@pytest.mark.skip(reason="insere um usuario no banco de verdade")
async def test_insert_user():
    user_info = {
        "user_name": "John Doe",
        "age": 99,
        "uf": "SP"
    }
    users_repository = UsersRepository()
    await users_repository.insert_user(user_info)


@pytest.mark.asyncio
@pytest.mark.skip(reason="busca um usuario no banco de verdade")
async def test_get_user_by_id():
    users_repository = UsersRepository()
    user_id = 1
    user = await users_repository.get_user_by_id(user_id)
    assert user is not None
    assert user["id"] == 1
