# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:

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
    import csv 
    f = open("products.csv","r",newline="")
    reader = csv.reader(f)

    for row in reader: 
        print(row) 

    import csv 
    f = open("order.csv","r",newline="")
    reader = csv.reader(f)

    for row in reader: 
        print(row) 

    f.close()

# Test your code here
result = calculate_order_total("products.csv", "order.csv", "total.csv")
print(f"Grand total: ${result:.2f}")
