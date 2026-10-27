from sqlalchemy.orm.exc import NoResultFound

from ..entities.people import PeopleTable
from ..entities.pets import PetsTable
from ..interfaces.people_repository_interface import PeopleRepositoryInterface
from ..settings.connection import DBConnectionHandler
from ....dtos.create_people_dto import CreatePeopleDTO
from ....dtos.people_with_pet_dto import PeopleWithPetDTO
from ....dtos.response_people_dto import ResponsePeopleDTO


class PeopleRepository(PeopleRepositoryInterface):
    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__db_connection = db_connection

    def insert_people(self, people: CreatePeopleDTO) -> ResponsePeopleDTO:
        with self.__db_connection as database:
            try:
                people_entity = PeopleTable(
                    first_name=people.first_name,
                    last_name=people.last_name,
                    age=people.age,
                    pet_id=people.pet_id
                )

                database.session.add(people_entity)
                database.session.commit()

                database.session.refresh(people_entity)

                response_people = ResponsePeopleDTO.model_validate(people_entity)

                return response_people
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
