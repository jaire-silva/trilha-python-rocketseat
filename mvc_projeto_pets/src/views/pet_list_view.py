from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..controllers.interfaces.pet_list_controller_interface import PetListControllerInterface


class PetListView(ViewInterface):

    def __init__(self, controller: PetListControllerInterface) -> None:
        self.__controller = controller

    def render(self, request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.get_pets()

        return HttpResponse(
            status_code=200,
            body=body_response
        )
