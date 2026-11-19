import pytest
from sqlalchemy import text

from fast_api_crud_de_usuario.src.models.settings.database_connection_handler import DBConnectionHandler


@pytest.mark.asyncio
async def test_connection():
    async with DBConnectionHandler() as db_handler:
        print(db_handler.session)
        assert db_handler.session is not None

        result = await db_handler.session.execute(text("SELECT 1"))
        assert result.scalar() == 1
