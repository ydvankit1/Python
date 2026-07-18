from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id: int 
    name: str=Field(
        ...,   # means compulsory
        min_length=3,
        max_length=50,
        description="Employee Name"
    )
    department: Optional[str]='General'