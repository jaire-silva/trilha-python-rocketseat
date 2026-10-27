from ..models.postgre.interfaces.people_repository_interface import PeopleRepositoryInterface

class PeopleCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface):
        self.people_repository = people_repository
