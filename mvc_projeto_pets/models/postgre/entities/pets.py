from sqlalchemy import BIGINT

from ..settings.connection import db


class Pets(db.Model):
    __tablename__: str = "pets"

    id = db.Column(BIGINT, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    type = db.Column(db.String(100), nullable=False, unique=False)

    def __repr__(self) -> str:
        return f"<Pets[id={self.id}, name={self.name}, type={self.type}]>"
