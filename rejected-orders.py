orders = [
    {"order_id": 601, "product": "Milk", "quantity": 2},
    {"order_id": 602, "product": "Bread", "quantity": 0},
    {"order_id": 603, "product": "Coffee", "quantity": -2},
    {"order_id": 604, "product": "Tea", "quantity": 4},
    {"order_id": 605, "product": "Cheese", "quantity": 1},
]

invalid_orders = []

for order in orders:
    if order["quantity"] <= 0:
        # Add the invalid order ID to invalid_orders
        invalid_orders.append(order["order_id"])


print(len(invalid_orders))
# print(invalid_orders)

valid_count = len(orders) - len(invalid_orders)
# print(valid_count)

print("Total orders:", len(orders))
print("Valid orders:", valid_count)
print("InValid orders:", len(invalid_orders))
print("Invalid order records:", invalid_orders)
