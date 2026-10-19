from flask import Blueprint, jsonify

from design_de_codigo.src.errors.http_bad_request import HttpBadRequestError
from design_de_codigo.src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

errors_bp = Blueprint('errors', __name__)


@errors_bp.app_errorhandler(HttpBadRequestError)
def handle_http_bad_request_error(error: HttpBadRequestError):
    response = {
        "success": False,
        "status_code": error.status_code,
        "body": {
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        }
    }

    return jsonify(response), error.status_code


@errors_bp.app_errorhandler(HttpUnprocessableEntityError)
def handle_unprocessable_entity(error: HttpUnprocessableEntityError):
    response = {
        "success": False,
        "status_code": error.status_code,
        "body": {
            "errors": [{
                "title": error.name,
                "detail": error.message
            }]
        }
    }
    return jsonify(response), error.status_code