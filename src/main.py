import src.io.csv as csv
import src.config.config as config
from src.request.magento_request import MagentoRequest
import warnings
import json
import src.model.Order.Item.ItemIDMap as ItemIDMap


def main():
    request = MagentoRequest()
    filename = config.data_path + config.input_file_name

    for order in csv.generateOrdersFromCsv(filename):
        response = request.createEntity(order, 'order')
        response_content = json.loads(response.content.decode())

        if response.status_code == 200:
            print(f"Order {order.name} successfully created")

            order.magento_id = response_content['entity_id']

            # We need to remember the original ID's of items, and the item ID that magento has generated.
            # This is necessary for invoices and other API requests - so we map them in this data structure.
            ItemIDMap.generateIdMap(response_content['items'])

            for invoice_id, invoice in order.invoices.items():
                invoice_response = request.createEntity(invoice, 'invoice', order.magento_id)
                print(f"Invoice request returned {invoice_response.status_code}")

            for shipment_id, shipment in order.shipments.items():
                shipment_response = request.createEntity(shipment, 'shipment', order.magento_id)
                print(f"Shipment request returned {shipment_response.status_code}")

            for refund_id, refund in order.refunds.items():
                refund_response = request.createEntity(refund, 'refund', order.magento_id)
                print(f"Refund request returned {refund_response.status_code}")

        else:
            error_message = json.loads(response.content.decode())['message']
            print(f"Order {order.name} could not be created, there was an error: "
                  f"{response.reason} -> {error_message}")


if __name__ == "__main__":
    warnings.simplefilter('ignore')
    try:
        main()
    except FileNotFoundError:
        print(f"The script couldn't open the file: {config.data_path + config.input_file_name}")
