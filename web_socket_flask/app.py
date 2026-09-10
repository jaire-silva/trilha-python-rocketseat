import os

from flask import Flask

from web_socket_flask.database import db
from web_socket_flask.payment.route import bp_payment

app = Flask(__name__)

app.config["SECRET_KEY"] = "admin123"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:admin123@localhost:5432/web_socket_flask"

db.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

app.register_blueprint(bp_payment)

with app.app_context():
    db.create_all()
    db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)