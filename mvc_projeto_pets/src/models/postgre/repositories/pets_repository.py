from typing import List

from sqlalchemy.exc import NoResultFound

from ..entities.pets import PetsTable
from ..interfaces.pets_repository_interface import PetsRepositoryInterface
from ..settings.connection import DBConnectionHandler


class PetsRepository(PetsRepositoryInterface):
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
            except Exception as exc:
                database.session.rollback()
                raise exc

    def delete_pet(self, pet_id: int) -> None:

        with self.__db_connection as database:
            try:
                database.session.query(PetsTable).filter(PetsTable.id == pet_id).delete()
            except Exception as exc:
                database.session.rollback()
                raise exc
