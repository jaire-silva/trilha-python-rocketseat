from pydantic import ValidationError

from mvc_projeto_pets.src.dtos.people_create_dto import PeopleCreateDTO
from mvc_projeto_pets.src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from mvc_projeto_pets.src.views.http_types.http_request import HttpRequest


def people_creator_validator(http_request: HttpRequest) -> None:
    try:
        PeopleCreateDTO(**http_request.body)
    except ValidationError as exc:
        raise HttpUnprocessableEntityError(exc.errors()) from exc
