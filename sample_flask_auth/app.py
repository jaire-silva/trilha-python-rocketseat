import os

import bcrypt
from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

from sample_flask_auth.database import db
from sample_flask_auth.enum.user_type import UserType
from sample_flask_auth.model.user import User

app = Flask(__name__)
logging_manager = LoginManager()

basedir = os.path.abspath(os.path.dirname(__file__))
instance_path = os.path.join(basedir, "instance")
os.makedirs(instance_path, exist_ok=True)
database_path = os.path.join(instance_path, "database.db")

app.config["SECRET_KEY"] = "admin123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin123@localhost:5432/sample_flask_auth"

db.init_app(app)

logging_manager.init_app(app)
logging_manager.login_view = "login"

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")

    existing_user = User.query.filter_by(username="admin").first()
    if existing_user:
        print("Usuário 'admin' já existe!")
    else:
        hashed_password = bcrypt.hashpw(str.encode("pass123"), bcrypt.gensalt())
        user = User(username="admin", password=hashed_password, role=UserType.ADMIN)

        db.session.add(user)
        db.session.commit()
        print("Usuário criado com sucesso!")


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

    if not user or not bcrypt.checkpw(str.encode(password), str.encode(user.password)):
        return jsonify({"message": "Credenciais inválidas"}), 400

    login_user(user)
    print(current_user.is_authenticated)

    return jsonify({"message": "Credenciais válidas"}), 200


@app.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logout realizado com sucesso"}), 200


@app.route("/user", methods=["POST"])
@login_required
def create_user():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Dados inválidos"}), 422

    isUserExists = User.query.filter_by(username=username).first()

    if isUserExists:
        return jsonify({"message": "Nome de usuário já existente"}), 409

    hashed_password = bcrypt.hashpw(str.encode(password), bcrypt.gensalt())
    user = User(username=username, password=hashed_password, role=UserType.USER)

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "Usuário cadastrado com sucesso!",
        "user": {"username": user.username, "id": user.id, "role": user.role}
    }), 200


@app.route("/user/<int:user_id>", methods=["GET"])
@login_required
def get_user(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404

    return jsonify({
        "user": {"username": user.username, "id": user.id, "role": user.role}
    })


@app.route("/user/<int:user_id>", methods=["PUT"])
@login_required
def update_user(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404

    if current_user.role != UserType.ADMIN:
        return jsonify({"message": "Acesso negado!"}), 403

    data = request.json
    username = data.get("username")
    password = data.get("password")

    db.session.query(User).filter(User.id == user_id).update({"username": username, "password": password})
    db.session.commit()

    return jsonify({
        "message": "Usuário atualizado com sucesso!",
        "user": {"username": user.username, "id": user.id, "role": user.role}
    })


@app.route("/user/<int:user_id>", methods=["DELETE"])
@login_required
def delete_user(user_id: int):
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "Usuário não encontrado."}), 404

    if current_user.id == user_id:
        return jsonify({"message": "Deleção não permitida!"}), 403

    if current_user.role != UserType.ADMIN:
        return jsonify({"message": "Acesso negado!"}), 403

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "Usuário deletado com sucesso!",
        "user": {"username": user.username, "id": user.id, "role": user.role}
    })


if __name__ == "__main__":
    app.run(debug=True)