from typing import List

from sqlalchemy.exc import NoResultFound

from mvc_projeto_pets.src.dtos.response_pet_dto import ResponsePetDTO
from ..entities.pets import PetsTable
from ..interfaces.pets_repository_interface import PetsRepositoryInterface
from ..settings.connection import DBConnectionHandler


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List[ResponsePetDTO]:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()

                response = [ResponsePetDTO.model_validate(pet) for pet in pets]

                return response

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
