from src.model.AbstractModel import AbstractModel


class Discount(AbstractModel):
    def __init__(self):
        # Discount data
        self.line_title = None
        self.line_name = None
        self.line_discount = None

    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:
        return {
                "comment": f"Discount - {self.line_title} - {self.line_name}: {self.line_discount}"
        }