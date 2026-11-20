orders = [
    {"order_id": 301, "product": "Cheese", "quantity": 3},
    {"order_id": 302, "product": "Coffee", "quantity": 0},
    {"order_id": 303, "product": "Tea", "quantity": -1},
]

for order in orders:

    if order["quantity"] <= 0:
        print("Invalid quantity for order:", order["order_id"])
    
    else:
        print("Valid quantity for order:", order["order_id"])