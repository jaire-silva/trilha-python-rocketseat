import os

# Diretório base da aplicação
BASEDIR_FOLDER = os.path.abspath(os.path.dirname(__file__))

# Caminhos das pastas estáticas
STATIC_FOLDER = os.path.join(BASEDIR_FOLDER, "static")
IMG_FOLDER = os.path.join(STATIC_FOLDER, "img")

# Cria as pastas se não existirem
os.makedirs(IMG_FOLDER, exist_ok=True)


def is_valid_qr_code_file(file_path):
    return os.path.isfile(file_path) and file_path.endswith(".png")