from flask import Flask

from sample_flask_auth.database import db
from sample_flask_auth.model.user import User

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(debug=True)