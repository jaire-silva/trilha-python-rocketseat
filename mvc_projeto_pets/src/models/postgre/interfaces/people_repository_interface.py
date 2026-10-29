from abc import ABC
from abc import abstractmethod

from ....dtos.people_create_dto import PeopleCreateDTO
from ....dtos.people_with_pet_dto import PeopleWithPetDTO
from ....dtos.response_people_dto import ResponsePeopleDTO


class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_people(self, people: PeopleCreateDTO) -> ResponsePeopleDTO:
        pass

    @abstractmethod
    def get_people_by_id(self, people_id: int) -> PeopleWithPetDTO | None:
        pass
