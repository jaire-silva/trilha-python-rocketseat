from abc import ABC, abstractmethod


class PetListControllerInterface(ABC):
    @abstractmethod
    def get_pets(self) -> dict:
        pass
