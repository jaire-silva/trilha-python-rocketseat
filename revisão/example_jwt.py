from datetime import datetime, timedelta, timezone

import jwt
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    return "Hello, World!"


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(minutes=50),
            "email": "jaire@email.com"
        },
        key="minhaChave",
        algorithm="HS256"
    )
    return jsonify({"token": token}), 200


@app.route("/secret", methods=["POST"])
def secret():
    raw_token = request.headers.get("Authorization")
    token = raw_token.split(" ")[1]

    try:
        token_information = jwt.decode(token, "minhaChave", algorithms="HS256")
        print(token_information)
    except Exception as exc:
        return jsonify({"erro": str(exc)}), 400

    return jsonify({"secret": "segredo"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
