from ..dtos.response_pet_dto import ResponsePetDTO
from ..models.postgre.repositories.pets_repository import PetsRepositoryInterface


class PetListController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.pets_repository = pets_repository

    def get_pets(self) -> dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)
        return response

    def __get_pets_in_db(self) -> list[ResponsePetDTO]:
        pets = self.pets_repository.list_pets()
        return pets

    def __format_response(self, pets: list[ResponsePetDTO]) -> dict:
        formatted_pets = []

        for pet in pets:
            formatted_pets.append(pet.model_dump())

        return {
            "data": {
                "type": "Pets",
                "count": len(pets),
                "attributes": formatted_pets
            }
        }
