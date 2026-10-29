from flask import Blueprint, jsonify, request

from mvc_projeto_pets.src.main.composer.people_creator_composer import people_creator_composer
from mvc_projeto_pets.src.main.composer.people_finder_composer import people_finder_composer
from mvc_projeto_pets.src.views.http_types.http_request import HttpRequest

people_route_bp = Blueprint('people_routes', __name__)


@people_route_bp.route('/people/create', methods=['POST'])
def create_person():
    http_request = HttpRequest(body=request.json)

    view = people_creator_composer()

    http_response = view.render(http_request)

    return jsonify(http_response.body), http_response.status_code


@people_route_bp.route('/people/<int:people_id>', methods=['GET'])
def get_person(people_id):
    http_request = HttpRequest(param={"people_id": people_id})

    view = people_finder_composer()

    http_response = view.render(http_request)

    return jsonify(http_response.body), http_response.status_code
