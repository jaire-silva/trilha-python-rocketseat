from flask import Flask

from design_de_codigo.src.main.routes.calculators import calc_route_bp

app = Flask(__name__)

app.register_blueprint(calc_route_bp)