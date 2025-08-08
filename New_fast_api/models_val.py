from pydantic import BaseModel,Field,StrictInt
from typing import List,Optional



class Employee(BaseModel):
    id:int=Field(...,gt=0,title='Employe Id')
    name:str=Field(...,min_length=3,max_length=30)
    department:str=Field(...,min_length=3,max_length=30)
    age:Optional[StrictInt]=Field(gt=0,default=18)