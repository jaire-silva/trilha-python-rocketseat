from ..models.postgre.repositories.pets_repository import PetsRepositoryInterface


class PetDeleteController:
    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self.pets_repository = pets_repository

    def delete_pet(self, pet_id: int) -> None:
        self.pets_repository.delete_pet(pet_id)
