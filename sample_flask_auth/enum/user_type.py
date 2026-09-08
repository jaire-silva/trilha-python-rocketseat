from enum import Enum, auto


class UserType(str, Enum):
    ADMIN = "ADMIN"
    USER = "USER"