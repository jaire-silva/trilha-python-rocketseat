from sqlalchemy.orm.exc import NoResultFound

from ..entities.people import PeopleTable
from ..entities.pets import PetsTable
from ..settings.connection import DBConnectionHandler
from ....dtos.people_with_pet_dto import PeopleWithPetDTO


class PeopleRepository:
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_people(self, people: PeopleTable) -> PeopleTable:
        with self.__db_connection as database:
            try:
                database.session.add(people)
                database.session.commit()
                database.session.refresh(people)
                return people
            except Exception as exc:
                database.session.rollback()
                raise exc

    def get_people_by_id(self, people_id: int) -> PeopleWithPetDTO | None:
        with self.__db_connection as database:
            try:
                row = (
                    database
                    .session
                    .query(PeopleTable)
                    .outerjoin(PetsTable, PetsTable.id == PeopleTable.pet_id)
                    .filter(PeopleTable.id == people_id)
                    .with_entities(
                        PeopleTable.first_name,
                        PeopleTable.last_name,
                        PetsTable.name.label("pet_name"),
                        PetsTable.type.label("pet_type")
                    ).one()
                )
                return PeopleWithPetDTO.model_validate(row)

            except NoResultFound:
                return None
