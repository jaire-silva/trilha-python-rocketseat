from sqlalchemy import Integer, String, Column

from ..settings.base import Base


class PetsTable(Base):
    __tablename__: str = "pets"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), nullable=False, unique=False)
    type = Column(String(200), nullable=False, unique=False)

    def __repr__(self) -> str:
        return f"<Pets[id={self.id}, name={self.name}, type={self.type}]>"
