from ..controllers.pet_delete_controller import PetDeleteController


def test_pet_delete_controller_delete_pet_pass(mocker):
    mock_repository = mocker.Mock()

    controller = PetDeleteController(mock_repository)
    controller.delete_pet(1)

    mock_repository.delete_pet.assert_called_once_with(1)
