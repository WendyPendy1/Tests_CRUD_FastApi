from pydantic import BaseModel, field_validator

class Games(BaseModel):
    numb: int
    name: str
    price: int
    descr: str

    @field_validator("name", "price")
    def name_price(cls, value):
        if value == "" or value is None:
            raise ValueError("Field is empty")
        else:
            return value

