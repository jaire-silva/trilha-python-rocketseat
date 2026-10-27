from abc import ABC
from abc import abstractmethod

from ....dtos.create_people_dto import CreatePeopleDTO
from ....dtos.people_with_pet_dto import PeopleWithPetDTO
from ....dtos.response_create_people_dto import ResponseCreatePeopleDTO


class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_people(self, people: CreatePeopleDTO) -> ResponseCreatePeopleDTO:
        pass

    @abstractmethod
    def get_people_by_id(self, people_id: int) -> PeopleWithPetDTO | None:
        pass
