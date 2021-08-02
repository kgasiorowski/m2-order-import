from src.model.Order.Item.Item import Item
import json


class Invoice:
    def __init__(self, invoice_id: int):
        self.id = invoice_id
        self.items = []

    def addItem(self, item: Item):
        self.items.append(item)

    def createRequestData(self, item_id_map: dict) -> str:
        item_data = []
        for item in self.items:
            item_data.append(item.createRequestData(item_id_map))
        request_payload = {"items": item_data}
        return json.dumps(request_payload)
