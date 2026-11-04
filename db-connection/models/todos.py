from pydantic import BaseModel

class database_pattern(BaseModel):
        name:str
        branch : str
        status :bool
        age : int