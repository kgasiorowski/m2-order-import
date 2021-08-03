from src.model.Order.Item.Item import Item
from src.model.AbstractModel import AbstractModel


class Invoice(AbstractModel):
    def __init__(self, invoice_id: int):
        self.id = invoice_id
        self.items = []

    def addItem(self, item: Item):
        self.items.append(item)

    def getStructuredPayloadData(self) -> dict:
        request_payload = {
            "items": [item.getSubRequestFormattedData() for item in self.items]
        }
        return request_payload
