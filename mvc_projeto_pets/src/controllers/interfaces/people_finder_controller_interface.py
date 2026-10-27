from abc import ABC, abstractmethod


class PeopleFinderControllerInterface(ABC):
    @abstractmethod
    def find_by_id(self, people_id: int) -> dict:
        pass
