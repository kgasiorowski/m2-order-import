from src.model.Order.Item.Item import Item
from src.model.AbstractModel import AbstractModel


class Invoice(AbstractModel):
    def __init__(self, invoice_id: int):
        self.id = invoice_id
        self.items = []

    def addItem(self, item: Item):
        self.items.append(item)

    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:
        item_data = []
        for item in self.items:
            item_data.append(item.getStructuredPayloadData(item_id_map))
        request_payload = {"items": item_data}
        return request_payload
