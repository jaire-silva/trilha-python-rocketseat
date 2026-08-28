import os

from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user

from sample_flask_auth.database import db
from sample_flask_auth.model.user import User

app = Flask(__name__)
logging_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, "instance")
os.makedirs(instance_path, exist_ok=True)
database_path = os.path.join(instance_path, "database.db")

app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"

db.init_app(app)

logging_manager.init_app(app)
logging_manager.login_view = "login"

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")


@app.route("/")
def hello_world():
    return "Hello, World!"


@logging_manager.user_loader
def load_user(user_id: int):
    return User.query.get(int(user_id))


@app.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Credenciais inválidas"}), 400

    user: User = User.query.filter_by(username=username).first()

    if not user or user.password != password:
        return jsonify({"message": "Credenciais inválidas"}), 400

    login_user(user)
    print(current_user.is_authenticated)

    return jsonify({"message": "Credenciais válidas"}), 200


if __name__ == "__main__":
    app.run(debug=True)