from src.model.AbstractModel import AbstractModel


class Order(AbstractModel):
    def __init__(self):
        self.items = []
        self.discounts = []
        self.invoices = {}
        self.shipments = {}
        self.refunds = {}

        self.original_id = None
        self.magento_id = None

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

    def getStructuredPayloadData(self, item_id_map: dict = None) -> dict:

        item_data = []
        for item in self.items:
            item_data.append(item.getStructuredPayloadData())

        discount_data = []
        for discount in self.discounts:
            discount_data.append({
                "comment": f"Discount - {discount.line_title} - {discount.line_name}: {discount.line_discount}"
            })

        return {
            "entity": {
                "base_currency_code": self.currency,
                "base_discount_amount": 0,
                "base_grand_total": self.price_total,
                "base_shipping_amount": 0,
                "base_shipping_incl_tax": 0,
                "base_shipping_tax_amount": 0,
                "base_shipping_discount_amount": 0,
                "base_subtotal": self.price_subtotal,
                "base_subtotal_incl_tax": 29.99,
                "base_total_due": 0,
                "base_total_paid": self.price_total,
                "base_to_global_rate": 1,
                "base_to_order_rate": 1,
                "created_at": self.created_at,
                "customer_email": self.customer_email,
                "customer_firstname": self.customer_first_name,
                "customer_group_id": 1,
                "customer_lastname": self.customer_last_name,
                "email_sent": 1,
                "global_currency_code": self.currency,
                "grand_total": self.price_total,
                "increment_id": self.name,
                "order_currency_code": self.currency,
                "state": "new",
                "status": self.payment_status,
                "store_currency_code": self.currency,
                "store_to_base_rate": 0,
                "store_to_order_rate": 0,
                "store_id": 1,
                "subtotal": self.price_subtotal,
                "subtotal_incl_tax": self.price_subtotal,
                "total_due": 0,
                "total_paid": self.price_total,
                "weight": self.weight_total,
                "updated_at": self.updated_at,
                "items": item_data,
                "billing_address": {
                    "address_type": "billing",
                    "city": self.billing_city,
                    "company": self.billing_company,
                    "country_id": self.billing_country_code,
                    "customer_address_id": 4,
                    "email": self.customer_email,
                    "firstname": self.billing_first_name,
                    "lastname": self.billing_last_name,
                    "postcode": self.billing_zip,
                    "region": self.billing_province_code,
                    "street": [
                        self.billing_address_1 + " " + self.billing_address_2
                    ],
                    "telephone": self.billing_phone
                },
                "payment": {
                    "amount_paid": self.price_total,
                    "method": "checkmo"
                },
                "status_histories": discount_data,
                "extension_attributes": {
                    "shipping_assignments": [{
                        "shipping": {
                            "address": {
                                "address_type": "shipping",
                                "city": self.shipping_city,
                                "company": self.shipping_company,
                                "country_id": self.shipping_country_code,
                                "customer_address_id": 4,
                                "email": self.customer_email,
                                "firstname": self.shipping_first_name,
                                "lastname": self.shipping_last_name,
                                "postcode": self.shipping_zip,
                                "region": self.shipping_province_code,
                                "street": [
                                    self.shipping_address_1 + " " + self.shipping_address_2
                                ],
                                "telephone": self.shipping_phone
                            }
                        }
                    }],
                    "applied_taxes": [],
                    "item_applied_taxes": [],
                    "converting_from_quote": False,
                    "send_notification": 0
                }
            }
        }
