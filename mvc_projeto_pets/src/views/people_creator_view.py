from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..controllers.interfaces.people_creator_controller_interface import PeopleCreatorControllerInterface


class PeopleCreatorView(ViewInterface):

    def __init__(self, controller: PeopleCreatorControllerInterface) -> None:
        self.__controller = controller

    def render(self, request: HttpRequest) -> HttpResponse:
        people_info = request.body
        body_response = self.__controller.create(people_info)

        return HttpResponse(
            status_code=201,
            body=body_response
        )
