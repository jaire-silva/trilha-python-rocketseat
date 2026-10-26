CREATE TABLE IF NOT EXISTS "pets" (
    id SERIAL PRIMARY KEY ,
    name VARCHAR(200) NOT NULL,
    type VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS "people" (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    age INTEGER NOT NULL,
    pet_id INTEGER NOT NULL,
    FOREIGN KEY (pet_id) REFERENCES pets(id)
);

INSERT INTO pets (name, type)
VALUES
    ('cobra', 'snake'),
    ('cao', 'dog'),
    ('gato', 'cat'),
    ('jorgin', 'hamster'),
    ('burro', 'donkey'),
    ('shrek', 'ogro'),
    ('belinha', 'dog');