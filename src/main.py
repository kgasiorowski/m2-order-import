import src.io.csv as csv
import src.config.config as config
from src.request.magento_request import MagentoRequest
import warnings
import json


def main():
    request = MagentoRequest()
    filename = config.data_path + config.input_file_name

    for order in csv.generateOrdersFromCsv(filename):
        response = request.createOrder(order)
        response_content = json.loads(response.content.decode())

        if response.status_code == 200:
            print(f"Order {order.name} successfully created")

            order.magento_id = response_content['entity_id']

            # We need to remember the original ID's of items, and the item ID that magento has generated.
            # This is necessary for invoices and other API requests - so we map them in this data structure.
            # Line ID -> Entity ID
            item_id_map = {}
            for item in response_content['items']:
                item_id_map[int(item['additional_data'])] = item['item_id']

            for invoice_id, invoice in order.invoices.items():
                invoice_response = request.createInvoice(invoice, order, item_id_map)
                print(f"Invoice request returned {invoice_response.status_code}")


        else:
            error_message = json.loads(response.content.decode())['message']
            if 400 <= response.status_code < 500:
                print(f"Order {order.name} could not be created, there was an error: "
                      f"{response.reason} -> {error_message}")
            elif response.status_code > 500:
                print(f"Order {order.name} could not be created, there was a server error: "
                      f"{response.reason} -> {error_message}")


if __name__ == "__main__":
    warnings.simplefilter('ignore')
    try:
        main()
    except FileNotFoundError:
        print(f"The script couldn't open the file: {config.data_path + config.input_file_name}")
