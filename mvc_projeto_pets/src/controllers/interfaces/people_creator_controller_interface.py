from abc import ABC, abstractmethod


class PeopleCreatorControllerInterface(ABC):

    @abstractmethod
    def create(self, people_info: dict) -> dict:
        pass
