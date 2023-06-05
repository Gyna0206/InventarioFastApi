from pydantic import BaseModel, Field
from typing import Optional


class Product(BaseModel):
    id : Optional[int] = None
    name : str = Field(max_length=15, min_length=3, description="Nombre del producto")
    brand : str = Field(max_length=15, min_length=3, description="Marca del producto")
    description : str = Field(max_length=50, min_length= 1, description="descripcion del producto")
    price : float = Field(le=100000,description="Precio del producto")
    entry_date : str=Field(description="fecha de entrega")
    availability: str =Field(description="si o no disponible")
    available_quantity: int =Field(ge=0)

    
    class Config:
        schema_extra = {
            "example":{
                "id":1,
                "name":"gaseosa",
                "brand":"cocacola",
                "description":"gaseosa 1.5 sabor original",
                "price":5000,
                "entry_date":"4 de febrero",
                "availability":"si",
                "available_quantity":25
            }
        }