import pytest

from .people_creator_controller import PeopleCreatorController
from ..dtos.create_people_dto import CreatePeopleDTO
from ..dtos.response_create_people_dto import ResponseCreatePeopleDTO
from ..models.postgre.interfaces.people_repository_interface import PeopleRepositoryInterface


class MockPeopleRepository(PeopleRepositoryInterface):
    def insert_people(self, people: CreatePeopleDTO) -> ResponseCreatePeopleDTO:
        response = ResponseCreatePeopleDTO(
            id=1,
            first_name=people.first_name,
            last_name=people.last_name,
            age=people.age,
            pet_id=people.pet_id
        )
        return response

    def get_people_by_id(self, people_id: int) -> ResponseCreatePeopleDTO | None:
        pass


def test_people_creator_controller_create_pass():
    dto_test = {
        "first_name": "Jaire",
        "last_name": "Silva",
        "age": 20,
        "pet_id": 1
    }

    controller = PeopleCreatorController(MockPeopleRepository())

    response = controller.create(dto_test)

    dto_test_with_id = {"id": 1, **dto_test}

    assert response["data"]["type"] == "People"
    assert response["data"]["count"] == 1

    assert response["data"]["attributes"]["id"] == 1
    assert response["data"]["attributes"]["first_name"] == dto_test["first_name"]
    assert response["data"]["attributes"]["last_name"] == response["data"]["attributes"]["last_name"]
    assert response["data"]["attributes"]["age"] == response["data"]["attributes"]["age"]
    assert response["data"]["attributes"]["pet_id"] == response["data"]["attributes"]["pet_id"]
    assert response["data"]["attributes"] == dto_test_with_id


def test_people_creator_controller_create_error():
    dto_test = {
        "first_name": "Jaire123",
        "last_name": "Silva",
        "age": 20,
        "pet_id": 1
    }

    controller = PeopleCreatorController(MockPeopleRepository())

    with pytest.raises(Exception):
        controller.create(dto_test)
