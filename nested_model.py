from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str


class User(BaseModel):
    id: int
    name: str
    address: Address


# Creating Address object
address = Address(
    street="123 abc",
    city="abc"
)

# Creating User object
user = User(
    id=1,
    name="Ankit",
    address=address,
)

print(user)

# OR

user_data = {
    "id": 1,
    "name": "Ankit",
    "address": {
        "street": "123 abc",
        "city": "abc"
    }
}

user = User(**user_data)
print(user)