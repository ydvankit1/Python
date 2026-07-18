from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, 'name': "ankit", 'is_active':25}  # pydantic validate the data-type

user = User(**input_data)  # and also it require dictionary argument in unpacked way
print(user)   # Error: Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value=25, input_type=int]





# some other pydantic field

# user_id: int
# items=List[str]
# quantities: Dict[str, int]
# title: str
# content: str
# image_url: Optional[str]