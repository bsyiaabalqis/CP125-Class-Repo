# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv
def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    products = {}
    prod_file = open(products_file, "r", newline="")
    reader = csv.reader(prod_file)
    next(reader)  # Skip header
    for row in reader:
        product_id, name, price = row
        products[product_id] = (name, float(price))
    prod_file.close()

    # Read orders
    orders = []
    order_file_handle = open(order_file, "r", newline="")
    reader = csv.reader(order_file_handle)
    next(reader)  # Skip header
    for row in reader:
        product_id, quantity = row
        orders.append((product_id, int(quantity)))
    order_file_handle.close()

    # Calculate and write output
    grand_total = 0.0
    output = open(output_file, "w", newline="")
    writer = csv.writer(output)
    writer.writerow(["product_id", "total_cost"])
    for product_id, quantity in orders:
        if product_id in products:
            name, price = products[product_id]
            cost = price * quantity
            grand_total += cost
            writer.writerow([product_id, f"{cost:.2f}"])
    output.close()
    return grand_total

# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
