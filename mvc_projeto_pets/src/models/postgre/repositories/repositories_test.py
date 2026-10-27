import pytest

from .people_repository import PeopleRepository
from .pets_repository import PetsRepository
from ..entities.pets import PetsTable
from ..settings.connection import db_connection_handler
from ....dtos.create_people_dto import CreatePeopleDTO

db_connection_handler.connect_to_db()


@pytest.mark.skip(reason="interação com o banco")
def test_list_pets() -> None:
    repo = PetsRepository(db_connection_handler)
    response = repo.list_pets()
    print(response)


@pytest.mark.skip(reason="interação com o banco")
def test_delete_pet() -> None:
    pet = PetsTable()
    pet.name = "pet1"
    pet.type = "cat"

    repo = PetsRepository(db_connection_handler)

    repo.create_pet(pet)

    repo.delete_pet(pet.id)


@pytest.mark.skip(reason="interação com o banco")
def test_create_people():
    people = CreatePeopleDTO(
        first_name="test name",
        last_name="test last",
        age=77,
        pet_id=2
    )

    repo = PeopleRepository(db_connection_handler)
    response = repo.insert_people(people)
    print(response)


@pytest.mark.skip(reason="interação com o banco")
def test_get_people_by_id():
    people_id = 1

    repo = PeopleRepository(db_connection_handler)
    response = repo.get_people_by_id(people_id)

    print()
    print(response.pet_name)
