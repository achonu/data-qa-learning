orders = [
{"order_id": 301, "customer":"Uzo", "product":"Cheese"},
{"order_id": 302, "customer":"Alex", "product":"Coffee"},
{"order_id": 303, "customer":"Sam", "product":"Tea"},
]

print(orders[0]["order_id"])
print(len(orders))

orders.append({"order_id": 304, "customer": "Mia", "product": "Milk"})
print(orders)

print(orders[3]["customer"])

 
order_to_validate = {
    "order_id": 305,
    "product": "Coffee",
    "quantity": 2
}


quantity = order_to_validate["quantity"]

if quantity <= 0:
    print("Invalid quantity for order:", order_to_validate["order_id"])
else:
    print("Valid quantity")


quantities = [3, 0, -1, 2]

for quantity in quantities:

    if quantity <= 0:
        print("Invalid quantity")

    else:
        print("Valid quantity")