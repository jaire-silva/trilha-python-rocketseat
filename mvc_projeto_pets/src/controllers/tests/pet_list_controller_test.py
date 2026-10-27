from mvc_projeto_pets.src.controllers.pet_list_controller import PetListController
from mvc_projeto_pets.src.dtos.response_pet_dto import ResponsePetDTO
from mvc_projeto_pets.src.models.postgre.entities.pets import PetsTable
from mvc_projeto_pets.src.models.postgre.repositories.pets_repository import PetsRepositoryInterface

mock_pets = [
    ResponsePetDTO(
        id=1,
        name="Fluffy",
        type="cat"
    ),
    ResponsePetDTO(
        id=9,
        name="Fluffy",
        type="cat"
    )
]


class MockPetsRepository(PetsRepositoryInterface):
    def list_pets(self) -> list[ResponsePetDTO]:
        return mock_pets

    def create_pet(self, pet: PetsTable) -> PetsTable | None:
        pass

    def delete_pet(self, pet_id: int) -> None:
        pass


def test_pet_list_controller_get_pets_pass():
    formatted_pets = []

    for pet in mock_pets:
        formatted_pets.append(pet.model_dump())

    expected_response = {
        "data": {
            "type": "Pets",
            "count": len(mock_pets),
            "attributes": formatted_pets
        }
    }

    controller = PetListController(MockPetsRepository())
    response = controller.get_pets()

    assert response == expected_response
