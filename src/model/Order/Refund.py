from src.model.AbstractModel import AbstractModel
from src.model.Order.Item.Item import Item


class Refund(AbstractModel):

    def __init__(self, refund_id: int):
        self.id = refund_id
        self.items = []
        self.adjustment_amount = None
        self.shipping_amount = None

    def addItem(self, item: Item):
        self.items.append(item)

    def getStructuredPayloadData(self) -> dict:
        refund_arguments = {}
        refund_arguments.setdefault("shipping_amount", self.shipping_amount)
        if self.adjustment_amount < 0:
            refund_arguments.setdefault("adjustment_positive", self.adjustment_amount)
        else:
            refund_arguments.setdefault("adjustment_negative", self.adjustment_amount)
        return {
            "items": [item.getSubRequestFormattedData() for item in self.items],
            "arguments": refund_arguments
        }
