import re

from .interfaces.people_creator_controller_interface import PeopleCreatorControllerInterface
from ..dtos.create_people_dto import CreatePeopleDTO
from ..dtos.response_people_dto import ResponsePeopleDTO
from ..models.postgre.interfaces.people_repository_interface import PeopleRepositoryInterface


class PeopleCreatorController(PeopleCreatorControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.people_repository = people_repository

    def create(self, people_info: dict) -> dict:
        people_dto = CreatePeopleDTO(
            first_name=people_info["first_name"],
            last_name=people_info["last_name"],
            age=people_info["age"],
            pet_id=people_info["pet_id"]
        )

        self.__validate_first_and_last_name(people_dto.first_name, people_dto.last_name)

        response = self.__insert_people_in_db(people_dto)

        return self.__format_response(response)

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão Regular para caracteres que não são letras
        non_valid_characters = re.compile(r'[^a-zA-Z ]')

        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise Exception("Nome da pessoa invalido!")

    def __insert_people_in_db(self, people_dto: CreatePeopleDTO) -> ResponsePeopleDTO:
        return self.people_repository.insert_people(people_dto)

    def __format_response(self, response: ResponsePeopleDTO) -> dict:
        return {
            "data": {
                "type": "People",
                "count": 1,
                "attributes": response.model_dump(),
            }
        }
