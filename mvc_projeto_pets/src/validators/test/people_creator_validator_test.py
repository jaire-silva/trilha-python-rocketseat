from mvc_projeto_pets.src.validators.people_creator_validator import people_creator_validator


class MockRequest:
    def __init__(self, body: dict) -> None:
        self.body = body


def test_people_creator_validator():
    request = MockRequest(body={
        "first_name": "Fulano",
        "last_name": "deTal",
        "age": 3,
        "pet_id": 7
    })

    people_creator_validator(request)
