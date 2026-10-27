from abc import ABC
from abc import abstractmethod
from typing import List

from mvc_projeto_pets.src.dtos.response_pet_dto import ResponsePetDTO
from ..entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[ResponsePetDTO]:
        pass

    @abstractmethod
    def create_pet(self, pet: PetsTable) -> PetsTable | None:
        pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> None:
        pass
