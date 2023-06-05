from pydantic import BaseModel, Field 
from typing import Optional 
 
class Supplies(BaseModel): 
     id: Optional[int] = None   
     supplier_id : int = Field (gen= 1, description="identificacion del proveedor") 
     product_id : int = Field (gen= 1, description="identificacion del producto") 
     purchase_price : int = Field ( description="precio de la compra") 
    
 
     class config: 
            schema_extra = { 
                "example":{ 
                    "id": 1,
                    "supplier_id":1,
                    "product_id": 1, 
                    "purchase_price":35000 
                    
                } 
            }