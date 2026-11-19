from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

CONNECTION_STRING = "postgresql+asyncpg://admin:admin123@localhost:5432/fast_api_crud_de_usuario"

engine = create_async_engine(
    url=CONNECTION_STRING,
    echo=True,
    pool_size=2,
    max_overflow=0,
    pool_timeout=30
)

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class DBConnectionHandler:
    def __init__(self):
        self.session: Optional[AsyncSession] = None

    async def __aenter__(self):
        self.session = AsyncSessionLocal()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()
