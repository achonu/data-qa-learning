def say_hello():
    print("Hello, FreshCart QA!")

say_hello()


def show_order_id(order_id):
    print("Checking order:", order_id)

show_order_id(890)

orders = [
    {"order_id": 801, "product": "Milk", "quantity": 2},
    {"order_id": 802, "product": "Bread", "quantity": 0},
    {"order_id": 803, "product": "Tea", "quantity": -1},
]
#  def show_quantity(order):
   #  print("Order quantity:", order["quantity"])

#  show_quantity(orders)

def validate_order(order):
    if order["quantity"] > 0:
        print("Valid order:", order["order_id"])
    else:
        print("Invalid order:", order["order_id"])
        

for order in orders:
    validate_order(order)