orders = [
    {"order_id": 301, "product": "Cheese", "quantity": 3},
    {"order_id": 302, "product": "Coffee", "quantity": 0},
    {"order_id": 303, "product": "Tea", "quantity": -1},
]

invalid_orders = []

for order in orders:
    if order["quantity"] <= 0:
        # Add the invalid order ID to invalid_orders
        invalid_orders.append(order["order_id"])

print(len(invalid_orders))
print(invalid_orders)