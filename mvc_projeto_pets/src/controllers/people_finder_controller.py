from ..dtos.people_with_pet_dto import PeopleWithPetDTO
from ..models.postgre.interfaces.people_repository_interface import PeopleRepositoryInterface


class PeopleFinderController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.people_repository = people_repository

    def find_by_id(self, people_id: int) -> dict:
        people = self.__find_by_id_in_db(people_id)
        response = self.__format_response(people)
        return response

    def __find_by_id_in_db(self, people_id: int) -> PeopleWithPetDTO | None:
        people = self.people_repository.get_people_by_id(people_id)

        if not people:
            raise Exception("Pessoa não encontrada!")

        return people

    def __format_response(self, people: PeopleWithPetDTO) -> dict:
        return {
            "data": {
                "type": "People",
                "count": 1,
                "attributes": people.model_dump(),
            }
        }
