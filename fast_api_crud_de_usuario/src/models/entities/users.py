from sqlalchemy import Table, Column, Integer, String

from fast_api_crud_de_usuario.src.models.settings.metadata import metadata

Users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_name", String(255), nullable=False),
    Column("age", Integer, nullable=False),
    Column("uf", String(2), nullable=False)
)
