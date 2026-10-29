from flask import Flask
from flask_cors import CORS

from mvc_projeto_pets.src.models.postgre.settings.connection import db_connection_handler
from ..routes.person_routes import person_route_bp
from ..routes.pets_routes import pet_route_bp

db_connection_handler.connect_to_db()
app = Flask(__name__)
CORS(app)
app.register_blueprint(pet_route_bp)
app.register_blueprint(person_route_bp)
