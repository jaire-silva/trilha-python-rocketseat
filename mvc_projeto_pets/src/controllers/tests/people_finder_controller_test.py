# pylint: disable=unused-argument

from mvc_projeto_pets.src.controllers.people_finder_controller import PeopleFinderController
from mvc_projeto_pets.src.dtos.create_people_dto import CreatePeopleDTO
from mvc_projeto_pets.src.dtos.people_with_pet_dto import PeopleWithPetDTO
from mvc_projeto_pets.src.dtos.response_people_dto import ResponsePeopleDTO
from mvc_projeto_pets.src.models.postgre.interfaces.people_repository_interface import PeopleRepositoryInterface

mock_people_with_pet = PeopleWithPetDTO(
    first_name="John",
    last_name="Doe",
    pet_name="Fluffy",
    pet_type="cat"
)


class MockPeopleRepository(PeopleRepositoryInterface):
    def insert_people(self, people: CreatePeopleDTO) -> ResponsePeopleDTO:
        pass

    def get_people_by_id(self, people_id: int) -> PeopleWithPetDTO | None:
        return mock_people_with_pet


def test_people_finder_controller_find_by_id_pass():
    expected_response = {
        "data": {
            "type": "People",
            "count": 1,
            "attributes": mock_people_with_pet.model_dump()
        }
    }

    controller = PeopleFinderController(MockPeopleRepository())

    response = controller.find_by_id(6)

    assert response == expected_response
