from models.supplies import Supplies as SuppliesModel 
from schemas.supplies import Supplies

class SuppliesService():
    def __init__(self, db):
        self.db = db
    
    def get_supplies(self):
        result = self.db.query(SuppliesModel).all()
        return result
    
    def create_supplies(self,supplies:SuppliesModel):
         new_supplies = SuppliesModel(
             supplier_id = supplies.supplier_id,
             product_id = supplies.product_id,
             purchase_price = supplies.purchase_price
         )
         

         self.db.add(new_supplies)
         self.db.commit()
         return

    
    def get_for_id(self,id:int):
         result = self.db.query(SuppliesModel).filter(SuppliesModel.id==id).first()
         return result
    
    def update_supplies(self,data:Supplies):
         supplies = self.db.query(SuppliesModel).filter(SuppliesModel.id==data.id).first()
         supplies.supplier_id=data.supplier_id
         supplies.product_id = data.product_id
         supplies.purchase_price = data.purchase_price
         self.db.commit()
         return
    
    def delete_supplies(self, id:int):
         self.db.query(SuppliesModel).filter(SuppliesModel.id==id).delete()
         self.db.commit()
         return