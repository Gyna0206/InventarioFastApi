from pydantic import BaseModel, Field
from typing import Optional

class Supplier(BaseModel):
     id : Optional[int] = None
     name : str = Field(max_length=15, min_length=3, description="Nombre proveedor")
     addres : str = Field(max_length=30, min_length=3, description="Direccion del proveedor")
     phone:int=Field(description="telefono fel proveedor")
     email : str = Field(max_length=20, min_length= 1, description="email del proveedor ")


     class Config:
            schema_extra = {
                "example":{
                    "id":1,
                    "name":"Juan Garcia",
                    "addres":"calle 35b  #4-46 Bogota",
                    "phone":3156547983,
                    "email":"juanga23@gmail.com"

                }
            }