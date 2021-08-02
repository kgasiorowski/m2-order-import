class Item:
    def __init__(self):
        self.original_id = None
        self.magento_id = None
        self.quantity = None
        self.price = None
        self.total = None
        self.variant_sku = None
        self.variant_weight = None
        self.name = None

    def createRequestData(self, item_id_map: dict) -> dict:
        return {
            'order_item_id': item_id_map[int(self.original_id)],
            'qty': int(self.quantity)
        }
