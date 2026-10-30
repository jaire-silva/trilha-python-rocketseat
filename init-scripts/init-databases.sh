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

# Função para executar um schema SQL em um banco de dados específico
apply_schema() {
    local db=$1
    local schema_file=$2
    echo "Aplicando o schema no banco de dados: $db"
    psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$db" -f "$schema_file"
}


# Chama a função para criar as suas duas bases de dados de forma isolada e segura
create_database "sample_flask_auth"
create_database "web_socket_flask"
create_database "mvc_projeto_pets"
create_database "jwt_api_banco"

# Aplicando o schema ao banco "mvc_projeto_pets"
apply_schema "mvc_projeto_pets" "/docker-entrypoint-initdb.d/mvc_projeto_pets_schema.sql"

