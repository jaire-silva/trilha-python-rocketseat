from flask import Flask

from web_soscket_flask.database import db
from web_soscket_flask.payment.route import bp_payment

app = Flask(__name__)

app.config["SECRET_KEY"] = "admin123"
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:admin123@127.0.0.1:3306/web_socket_flask"

db.init_app(app)

app.register_blueprint(bp_payment)

if __name__ == "__main__":
    app.run(debug=True)