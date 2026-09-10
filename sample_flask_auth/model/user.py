from flask_login import UserMixin

from sample_flask_auth.database import db
from sample_flask_auth.enum.user_type import UserType


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserType), nullable=False, default=UserType.USER)