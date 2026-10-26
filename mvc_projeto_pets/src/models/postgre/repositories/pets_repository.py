from typing import List

from sqlalchemy.exc import NoResultFound

from ..entities.pets import PetsTable
from ..settings.connection import DBConnectionHandler


class PetsRepository:
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[PetsTable]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets

            except NoResultFound:
                return []

    def create_pet(self, pet: PetsTable) -> PetsTable | None:
        with self.__db_connection as database:
            try:
                database.session.add(pet)
                database.session.commit()
                database.session.refresh(pet)
                return pet
            except Exception as e:
                database.session.rollback()
                print(f"Erro durante a criação do pet: {e}")
                return None

    def delete_pet(self, pet_id: int) -> None:

        with self.__db_connection as database:
            try:
                database.session.query(PetsTable).filter(PetsTable.id == pet_id).delete()
            except NoResultFound:
                database.session.rollback()
