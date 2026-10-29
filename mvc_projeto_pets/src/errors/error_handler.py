from flask import Blueprint, jsonify

from mvc_projeto_pets.src.errors.errors_types.error_interface import ErrorInterface
from mvc_projeto_pets.src.errors.errors_types.http_bad_request import HttpBadRequestError
from mvc_projeto_pets.src.errors.errors_types.http_not_found import HttpNotFoundError
from mvc_projeto_pets.src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntityError
from mvc_projeto_pets.src.views.http_types.http_response import HttpResponse

error_handler_bp = Blueprint('errors', __name__)


def __handle_error_body(error: ErrorInterface) -> dict:
    return {
        "errors": [{
            "title": error.name,
            "detail": error.message
        }]
    }


@error_handler_bp.app_errorhandler(HttpBadRequestError)
def handle_error_bad_request(error: HttpBadRequestError):
    response = HttpResponse(
        status_code=error.status_code,
        body=__handle_error_body(error)
    )

    return jsonify(response.body), response.status_code


@error_handler_bp.app_errorhandler(HttpNotFoundError)
def handle_error_not_found(error: HttpNotFoundError):
    response = HttpResponse(
        status_code=error.status_code,
        body=__handle_error_body(error)
    )

    return jsonify(response.body), response.status_code


@error_handler_bp.app_errorhandler(HttpUnprocessableEntityError)
def handle_error_unprocessable_entity(error: HttpUnprocessableEntityError):
    response = HttpResponse(
        status_code=error.status_code,
        body=__handle_error_body(error)
    )

    return jsonify(response.body), response.status_code


@error_handler_bp.app_errorhandler(Exception)
def handle_error_generic():
    response = HttpResponse(
        status_code=500,
        body={
            "errors": [{
                "title": "teste",
                "detail": "ver se funciona o erro"
            }]
        }
    )

    return jsonify(response.body), response.status_code
