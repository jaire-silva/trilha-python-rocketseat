from pydantic import BaseModel


class ResponsePetDTO(BaseModel):
    id: int
    name: str
    type: str

    class Config:
        from_attributes = True
