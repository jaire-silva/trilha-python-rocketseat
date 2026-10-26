from pydantic import BaseModel


class PeopleWithPetDTO(BaseModel):
    first_name: str
    last_name: str
    pet_name: str | None
    pet_type: str | None

    class Config:
        from_attributes = True  # Permite que o Pydantic leia dados direto de objetos do SQLAlchemy
