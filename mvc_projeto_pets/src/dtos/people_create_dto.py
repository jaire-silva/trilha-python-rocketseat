from pydantic import BaseModel, constr, conint


class PeopleCreateDTO(BaseModel):
    first_name: constr(min_length=1, max_length=255)
    last_name: constr(min_length=1, max_length=255)
    age: conint(ge=0)
    pet_id: conint(ge=1)

    class Config:
        from_attributes = True  # Permite que o Pydantic leia dados direto de objetos do SQLAlchemy
