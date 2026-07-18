from pydantic import BaseModel, field_validator

class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):  # v is the value enterd i.e, username
        if len(v)<4:
            raise ValueError("must be atleast 4 charchter")
        return v
        