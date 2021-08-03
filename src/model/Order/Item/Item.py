from src.model.AbstractModel import AbstractModel
import src.model.Order.Item.ItemIDMap as ItemIDMap


class Item(AbstractModel):
    def __init__(self):
        self.original_id = None
        self.magento_id = None
        self.quantity = None
        self.price = None
        self.total = None
        self.variant_sku = None
        self.variant_weight = None
        self.name = None

    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:
        return {
            "name": self.name,
            "original_price": self.price,
            "price": self.price,
            "price_incl_tax": self.price,
            "qty_ordered": self.quantity,
            "row_total": self.total,
            "row_total_incl_tax": self.total,
            "sku": self.variant_sku,
            "store_id": 1,
            "weight": self.variant_weight,
            "product_type": "simple",
            "additional_data": str(self.original_id)
        }

    def getOtherStructuredPayloadData(self) -> dict:
        item_id_map = ItemIDMap.getIdMap()
        return {
            'order_item_id': item_id_map[int(self.original_id)],
            'qty': int(self.quantity)
        }
