CREATE TABLE IF NOT EXISTS "users"
(
    id        SERIAL PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL,
    age       INTEGER      NOT NULL,
    uf        VARCHAR(2)   NOT NULL
);