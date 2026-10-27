from abc import ABC
from abc import abstractmethod
from typing import List

from ..entities.pets import PetsTable


class PetsRepositoryInterface(ABC):
    @abstractmethod
    def list_pets(self) -> List[PetsTable]:
        pass

    @abstractmethod
    def create_pet(self, pet: PetsTable) -> PetsTable | None:
        pass

    @abstractmethod
    def delete_pet(self, pet_id: int) -> None:
        pass
