import csv as py_csv
from src.model.Order.Order import Order
from src.model.Order.Item.Item import Item
from src.model.Order.Discount.Discount import Discount
from src.model.Order.Invoice import Invoice
from src.model.Order.Shipment import Shipment
from src.model.Order.Tracking.Tracking import Tracking
from src.model.Order.Refund import Refund
from collections import Iterable


def generateOrdersFromCsv(filename: str) -> Iterable:
    with open(filename, 'r', encoding='utf-8-sig') as raw_csv_file:

        csv_reader = py_csv.DictReader(raw_csv_file)
        order = None

        for line in csv_reader:
            if line['Top Row'] == 'TRUE':
                if order is None:
                    # If the order doesn't exist and we reach a top row,
                    # that means this is the first order in the file.
                    order = Order()
                    extractRowInformation(line, order)
                    continue
                # This signifies that a new order has been reached.
                # Yield our order object, and create a new one.
                yield order
                order = Order()
                extractRowInformation(line, order)
            else:
                extractRowInformation(line, order)
        # EOF - create an order from whatever's left
        yield order


def extractRowInformation(line: dict, order: Order) -> None:
    line_type = line['Line: Type']

    if line_type == 'Line Item':
        processItemLineType(line, order)
    elif line_type == 'Discount':
        processDiscountLineType(line, order)
    elif line_type == 'Shipment':
        processShipmentLineType(line, order)
    elif line_type == 'Credit Memo':
        processCreditMemoLineType(line, order)


def processCreditMemoLineType(line: dict, order: Order) -> None:
    credit_memo_id = int(line['Credit Memo: ID'])
    order.refunds.setdefault(credit_memo_id, Refund(credit_memo_id))
    order.refunds[credit_memo_id].adjustment_amount = int(line['Credit Memo: Adjustment amount'])
    order.refunds[credit_memo_id].shipping_amount = int(line['Credit Memo: Shipping amount'])


def processShipmentLineType(line: dict, order: Order) -> None:
    shipment_id = int(line['Shipment: ID'])
    order.shipments.setdefault(shipment_id, Shipment(shipment_id))
    track = Tracking()
    track.title = line['Shipment: Title']
    track.carrier_code = line['Shipment: Carrier Code']
    track.tracking_number = line['Shipment: Tracking Number']
    order.shipments[shipment_id].addTrack(track)


def processDiscountLineType(line: dict, order: Order) -> None:
    discount = Discount()
    discount.line_title = line['Line: Title']
    discount.line_name = line['Line: Name']
    discount.line_discount = line['Line: Discount']
    order.discounts.append(discount)


def processItemLineType(line: dict, order: Order) -> None:
    if line['Top Row']:
        # If this line item is the top row, then get all the general order details
        order.name = line['Name']
        order.created_at = line['Created At']
        order.updated_at = line['Updated At']
        order.cancelled_at = line['Cancelled At']
        order.cancel_reason = line['Cancel: Reason']
        order.currency = line['Currency']
        order.weight_total = line['Weight Total']
        order.price_total_line_items = line['Price: Total Line Items']
        order.price_subtotal = line['Price: Subtotal']
        order.price_total = line['Price: Total']
        order.payment_status = line['Payment: Status']
        order.customer_email = line['Customer: Email']
        order.customer_phone = line['Customer: Phone']
        order.customer_first_name = line['Customer: First Name']
        order.customer_last_name = line['Customer: Last Name']
        order.billing_first_name = line['Billing: First Name']
        order.billing_last_name = line['Billing: Last Name']
        order.billing_company = line['Billing: Company']
        order.billing_phone = line['Billing: Phone']
        order.billing_address_1 = line['Billing: Address 1']
        order.billing_address_2 = line['Billing: Address 2']
        order.billing_zip = line['Billing: Zip']
        order.billing_city = line['Billing: City']
        order.billing_province_code = line['Billing: Province Code']
        order.billing_country_code = line['Billing: Country Code']
        order.shipping_first_name = line['Shipping: First Name']
        order.shipping_last_name = line['Shipping: Last Name']
        order.shipping_company = line['Shipping: Company']
        order.shipping_phone = line['Shipping: Phone']
        order.shipping_address_1 = line['Shipping: Address 1']
        order.shipping_address_2 = line['Shipping: Address 2']
        order.shipping_phone = line['Shipping: Phone']
        order.shipping_zip = line['Shipping: Zip']
        order.shipping_city = line['Shipping: City']
        order.shipping_province_code = line['Shipping: Province Code']
        order.shipping_country_code = line['Shipping: Country Code']
        order.payment_gateway = line['Transaction: Gateway']
    # Add an item for this row
    item = Item()
    item.original_id = line['Line: ID']
    item.quantity = line['Line: Quantity']
    item.price = line['Line: Price']
    item.total = line['Line: Total']
    item.variant_sku = line['Line: Variant SKU']
    item.variant_weight = line['Line: Variant Weight']
    item.name = line['Line: Name']

    # Check if this line item is being invoiced
    invoice_id = int(line['Invoice: ID']) if line['Invoice: ID'] else None
    if invoice_id:
        order.invoices.setdefault(invoice_id, Invoice(invoice_id))
        order.invoices[invoice_id].addItem(item)

    shipment_id = int(line['Shipment: ID']) if line['Shipment: ID'] else None
    if shipment_id:
        order.shipments.setdefault(shipment_id, Shipment(shipment_id))
        order.shipments[shipment_id].addItem(item)

    credit_memo_id = int(line['Credit Memo: ID']) if line['Credit Memo: ID'] else None
    if credit_memo_id:
        order.refunds.setdefault(credit_memo_id, Refund(credit_memo_id))
        order.refunds[credit_memo_id].addItem(item)

    order.items.append(item)
