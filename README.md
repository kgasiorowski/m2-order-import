# m2-order-import

The purpose of this project is to provide a tool to import order history data for magento 2 sites.

## Usage Instructions

1. Create an integration in the magento backend. It should be enough to give it permissions for Sales, but if this does not work, just give it all permissions.
2. Enter the consumer key, consumer secret, access token, and access secret in the corresponding fields in secret.py. Do not commit this file. If you do, you will give anyone who has access to your repository access to whatever permissions you give your integration.
3. Run main.py. If the script can't open the file, you may need to mess with the file name and path in config.py.

## CSV Format

The CSV has the following format:
- Each line has a specific type, and each type represents a specific aspect of the order. Lines may have the following types:
  - `Line Item`
  - `Shipment`
  - `Credit Memo`
  - `Discount`
  - `Transaction`
- The order in which lines appear does not matter (within an order), so long as the main line item (with `Top Row` = TRUE) is first

### Invoices
- If you want to invoice an item in an order, supply an invoice ID in that Line Item's `Invoice: ID` column
- You may have multiple `Invoice`s per order

### Shipments
- If you want to add an item to a shipment, supply a shipment ID in that Line Item's `Shipment: ID` column
- For every shipment ID, there must be a `Shipment` type row which has a matching shipment ID. This row must have the `Shipment: Title`, `Shipment: Carrier Code`, and `Shipment: Tacking Number` columns populated
- If you want to specify multiple tracking numbers for a single shipment, you can add multiple `Shipment` type rows with the same ID. 
- **Please note that** in order to generate a shipment for an order, all items in that order must have been invoiced. Otherwise, the API will throw an error.
- You may have multiple `Shipment`s per order

### Credit Memos (refunds)
- If you'd like to refund a specific item in an order, supply a credit memo ID in that item's `Credit Memo: ID` column.
- Similarly to shipments, if any number of items is being refunded, you must add a `Credit Memo` line in that order. 
- You may have multiple `Credit Memo`s per order.
