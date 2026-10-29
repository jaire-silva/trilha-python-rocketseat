from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse
from .interfaces.view_interface import ViewInterface
from ..controllers.interfaces.people_finder_controller_interface import PeopleFinderControllerInterface


class PeopleFinderView(ViewInterface):

    def __init__(self, controller: PeopleFinderControllerInterface) -> None:
        self.__controller = controller

    def render(self, request: HttpRequest) -> HttpResponse:
        people_id = request.param["people_id"]
        body_response = self.__controller.find_by_id(people_id)

        return HttpResponse(
            status_code=200,
            body=body_response
        )
