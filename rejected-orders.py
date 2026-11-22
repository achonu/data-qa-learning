orders = [
    {"order_id": 901, "product": "Milk", "quantity": 0},
    {"order_id": 902, "product": "Bread", "quantity": -2},
    {"order_id": 903, "product": "Coffee", "quantity": -5},
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
