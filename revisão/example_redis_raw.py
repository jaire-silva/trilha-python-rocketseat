import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

redis_conn.set("chave_1", "algum_valor")
clave_1_valor = redis_conn.get("chave_1").decode('utf-8')
print(clave_1_valor)
print(type(clave_1_valor))

redis_conn.set("chave_1", "trocando_o_meu_valor")
clave_1_valor = redis_conn.get("chave_1").decode('utf-8')
print(clave_1_valor)
print(type(clave_1_valor))

# redis_conn.delete("chave_1")

# verificando se existe uma chave
chave_1_existe = redis_conn.exists("chave_1")
print()
print("=== chave_1_existe ===")
print("Existe:")
print(chave_1_existe)
print()

# comandos para hash
chave_hash = {
    "nome": "Jair",
    "idade": 25,
    "cidade": "sao paulo",
    "profissao": "Programador"
}

redis_conn.hset("chave_hash", "nome", "Jair")
redis_conn.hset("chave_hash", "idade", "25")
redis_conn.hset("chave_hash", "cidade", "sao paulo")
redis_conn.hset("chave_hash", "profissao", "Programador")

chave_hash_redis = redis_conn.hgetall("chave_hash")
print()
print("=== chave_hash_redis ===")
print(chave_hash_redis)
print(type(chave_hash_redis))
print()

# atualizando um valor
redis_conn.hset("chave_hash", "cidade", "curitiba")
chave_hash_redis = redis_conn.hgetall("chave_hash")
print()
print("=== chave_hash_redis atualizado ===")
print(chave_hash_redis)
print(type(chave_hash_redis))
print()

# pegando um valor
chave_hash_nome = redis_conn.hget("chave_hash", "nome").decode('utf-8')
print()
print("=== chave_hash_nome ===")
print(chave_hash_nome)
print(type(chave_hash_nome))

# deletando um valor
redis_conn.hdel("chave_hash", "profissao")
chave_hash_redis = redis_conn.hgetall("chave_hash")
print()
print("=== chave_hash_redis profissao deletado ===")
print(chave_hash_redis)
print(type(chave_hash_redis))

# buscando por existência de chave
chave_hash_nome_existe = redis_conn.hexists("chave_hash", "nome")
print()
print("=== chave_hash_nome_existe ===")
print(chave_hash_nome_existe)
print(type(chave_hash_nome_existe))

# utilizando o redis como cache, TTL = Time To Live
redis_conn.set("chave_cache", "esse valor sera deletado!", ex=12)

# adicionando tempo de ttl para hash já existente
redis_conn.expire("chave_hash", 30)
