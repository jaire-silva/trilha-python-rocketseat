from pydantic import BaseModel


class ResponsePeopleDTO(BaseModel):
    id: int
    first_name: str
    last_name: str
    age: int
    pet_id: int

    class Config:
        from_attributes = True
