from sqlalchemy import BigInteger, ForeignKey, String, Column

from ..settings.base import Base


class People(Base):
    __tablename__: str = "people"

    id = Column(BigInteger, primary_key=True)
    first_name = Column(String(100), nullable=False, unique=False)
    last_name = Column(String(100), nullable=False, unique=False)
    age = Column(BigInteger, nullable=False, unique=False)
    pet_id = Column(BigInteger, ForeignKey("pets.id"), nullable=False, unique=False)

    def __repr__(self) -> str:
        return (
            f"People[id={self.id}, first_name={self.first_name}, "
            f""f"last_name={self.last_name}, age={self.age}, pet_id={self.pet_id}]"
        )
