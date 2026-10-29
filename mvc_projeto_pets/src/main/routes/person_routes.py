from flask import Blueprint, jsonify, request

from mvc_projeto_pets.src.main.composer.people_creator_composer import people_creator_composer
from mvc_projeto_pets.src.views.http_types.http_request import HttpRequest

person_route_bp = Blueprint('person_routes', __name__)


@person_route_bp.route('/people/create', methods=['POST'])
def create_person():
    http_request = HttpRequest(body=request.json)

    view = people_creator_composer()

    http_response = view.render(http_request)

    return jsonify(http_response.body), http_response.status_code
