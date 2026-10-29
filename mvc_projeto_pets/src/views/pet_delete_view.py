from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..controllers.interfaces.pet_delete_controller_interface import PetDeleteControllerInterface


class PetDeleteView(ViewInterface):

    def __init__(self, controller: PetDeleteControllerInterface) -> None:
        self.__controller = controller

    def render(self, request: HttpRequest) -> HttpResponse:
        pet_id = request.param["pet_id"]
        self.__controller.delete_pet(pet_id)

        return HttpResponse(
            status_code=204,
            body={
                "data": {
                    "type": "Pets",
                    "message": "Pet deleted successfully!"
                }
            }
        )
