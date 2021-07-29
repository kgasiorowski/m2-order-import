class Order:
    def __init__(self):
        self.items = []
        self.discounts = []
        self.invoices = {}
        self.shipments = {}
        self.refunds = {}

        self.name = None
        self.note = None
        self.created_at = None
        self.updated_at = None
        self.cancelled_at = None
        self.cancel_reason = None
        self.currency = None
        self.weight_total = None
        self.price_total_line_items = None
        self.price_subtotal = None
        self.price_total = None
        self.payment_status = None
        
        self.customer_email = None
        self.customer_phone = None
        self.customer_first_name = None
        self.customer_last_name = None
        
        self.billing_first_name = None
        self.billing_last_name = None
        self.billing_company = None
        self.billing_phone = None
        self.billing_address_1 = None
        self.billing_address_2 = None
        self.billing_zip = None
        self.billing_city = None
        self.billing_province_code = None
        self.billing_country_code = None

        self.shipping_first_name = None
        self.shipping_last_name = None
        self.shipping_company = None
        self.shipping_phone = None
        self.shipping_address_1 = None
        self.shipping_address_2 = None
        self.shipping_zip = None
        self.shipping_city = None
        self.shipping_province_code = None
        self.shipping_country_code = None

    def createRequestData(self) -> str:
        ...
