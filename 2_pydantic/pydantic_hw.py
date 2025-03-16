from pydantic import BaseModel, EmailStr, Field, model_validator


class Address(BaseModel):
    city: str = Field(min_length=2)
    street: str = Field(min_length=3)
    house_number: int = Field(gt=0)


class User(BaseModel):
    name: str = Field(min_length=2, pattern=r"[A-Za-z]")
    age: int = Field(gt=0, lt=120)
    email: EmailStr
    is_employed: bool
    address: Address

    @model_validator(mode='before')
    @classmethod
    def check_raw_data(cls, data: dict[str, str]) -> dict[str, str]:
        age = int(data.get('age'))
        is_employed = data.get('is_employed')

        if is_employed and (age < 18 or age > 65):
            raise ValueError("You are not allowed to work!")

        return data

bad_user = """{

    "name": "John Doe",

    "age": 70,

    "email": "john.doe@example.com",

    "is_employed": true,

    "address": {

        "city": "New York",

        "street": "5th Avenue",

        "house_number": 123

    }

}"""

try:
    user = User.model_validate_json(bad_user)
    print(user)
except ValueError as e:
    print(e)

good_user = """{
    "name": "Jane Doe",
    "age": 20,
    "email": "jane.doe@example.com",
    "is_employed": true,
    "address": {
        "city": "Okhtyrka",
        "street": "Naugarder",
        "house_number": 6
    }
}"""
user = User.model_validate_json(good_user)
print(user)