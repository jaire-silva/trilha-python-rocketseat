from sqlalchemy import insert, select

from fast_api_crud_de_usuario.src.models.entities.users import Users
from fast_api_crud_de_usuario.src.models.settings.database_connection_handler import DBConnectionHandler


class UsersRepository:

    async def insert_user(self, user_info: dict):
        async with DBConnectionHandler() as db:
            query = insert(Users).values(**user_info)
            await db.session.execute(query)
            await db.session.commit()

    async def get_user_by_id(self, user_id: int):
        async with DBConnectionHandler() as db:
            query = select(Users).where(Users.columns.id == user_id)
            result = await db.session.execute(query)
            user = result.mappings().one_or_none()
            return dict(user) if user else None
