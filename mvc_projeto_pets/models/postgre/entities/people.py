from ..settings.connection import db


class People(db.Model):
    __tablename__: str = "people"

    id = db.Column(db.BigInteger, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False, unique=False)
    last_name = db.Column(db.String(100), nullable=False, unique=False)
    age = db.Column(db.BigInteger, nullable=False, unique=False)
    pet_id = db.Column(db.BigInteger, db.ForeignKey("pets.id"), nullable=False, unique=False)

    def __repr__(self) -> str:
        return (
            f"People[id={self.id}, first_name={self.first_name}, "
            f""f"last_name={self.last_name}, age={self.age}, pet_id={self.pet_id}]"
        )
