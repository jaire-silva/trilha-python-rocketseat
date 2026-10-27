from pydantic import BaseModel


class CreatePeopleDTO(BaseModel):
    first_name: str
    last_name: str
    age: int
    pet_id: int

    class Config:
        from_attributes = True  # Permite que o Pydantic leia dados direto de objetos do SQLAlchemy
