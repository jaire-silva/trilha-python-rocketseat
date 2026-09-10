#!/bin/bash
set -e

# Função que executa o comando SQL seguro diretamente no motor psql do Linux
create_database() {
    local db=$1
    echo "Verificando/Criando a base de dados: $db"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
        SELECT 'CREATE DATABASE $db'
        WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = '$db')\gexec
EOSQL
}

# Chama a função para criar as suas duas bases de dados de forma isolada e segura
create_database "sample_flask_auth"
create_database "web_socket_flask"