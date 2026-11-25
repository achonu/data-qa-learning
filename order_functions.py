
def show_order_id(order_id):
    print("Checking order:", order_id)

show_order_id(890)

orders = [
    {"order_id": 801, "product": "Milk", "quantity": 2},
    {"order_id": 802, "product": "Bread", "quantity": 0},
    {"order_id": 803, "product": "Tea", "quantity": -1},
]

def validate_order(order):

    if order["quantity"] > 0:
        return True 
    else:
        return False

rejected_ids = []
invalid_count = 0
valid_count = 0

for order in orders:
    result = validate_order(order) 
    if result == False:
      invalid_count +=1
      rejected_ids.append(order["order_id"])
    else:
        valid_count +=1  

print("Invalid orders:", invalid_count)
print("Valid orders:", valid_count)
print("Total orders:",len(orders))
print("Rejected orders IDs:", rejected_ids)

if valid_count + invalid_count == len(orders):
    print("Reconciliation passed")
else:
    print("Reconciliation failed")
    

if len(rejected_ids) == invalid_count:
    print("Rejected ID count passed")
else:
    print("Rejected ID count failed")
