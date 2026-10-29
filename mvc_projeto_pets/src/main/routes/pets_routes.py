from flask import Blueprint, jsonify

from mvc_projeto_pets.src.main.composer.pet_delete_composer import pet_delete_composer
from mvc_projeto_pets.src.main.composer.pet_list_composer import pet_list_composer
from mvc_projeto_pets.src.views.http_types.http_request import HttpRequest

pet_route_bp = Blueprint('pets_routes', __name__)


@pet_route_bp.route('/pets', methods=['GET'])
def list_pets():
    http_request = HttpRequest()
    view = pet_list_composer()

    http_response = view.render(http_request)

    return jsonify(http_response.body), http_response.status_code


@pet_route_bp.route('/pets/<int:pet_id>', methods=['DELETE'])
def delete_pet(pet_id):
    http_request = HttpRequest(param={"pet_id": pet_id})
    view = pet_delete_composer()

    http_response = view.render(http_request)

    return jsonify(http_response.body), http_response.status_code
