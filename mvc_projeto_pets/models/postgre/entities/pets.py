from sqlalchemy import BigInteger, String, Column

from ..settings.base import Base


class Pets(Base):
    __tablename__: str = "pets"

    id = Column(BigInteger, primary_key=True)
    name = Column(String(100), nullable=False, unique=False)
    type = Column(String(100), nullable=False, unique=False)

    def __repr__(self) -> str:
        return f"<Pets[id={self.id}, name={self.name}, type={self.type}]>"
