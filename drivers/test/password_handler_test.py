from ..password_handler import PasswordHandler


def test_encrypt_password():
    minha_senha = "123RocketENois"
    password_handler = PasswordHandler()

    hashed_password = password_handler.encrypt_password(minha_senha)

    password_check = password_handler.check_password(minha_senha, hashed_password)

    print(hashed_password)
    print(password_check)
