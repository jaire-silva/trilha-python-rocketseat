from abc import ABC
from abc import abstractmethod

from ..entities.people import PeopleTable
from ....dtos.people_with_pet_dto import PeopleWithPetDTO


class PeopleRepositoryInterface(ABC):
    @abstractmethod
    def insert_people(self, people: PeopleTable) -> PeopleTable:
        pass

    @abstractmethod
    def get_people_by_id(self, people_id: int) -> PeopleWithPetDTO | None:
        pass
