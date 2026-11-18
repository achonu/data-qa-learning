order = {
"order_id": 253,
"customer": "Uzo",
"product": "Cheese",
"quantity": 3,
"price": 2.50,
"is_valid": True,
}

total = order["price"] * order["quantity"]

print(order["customer"])
print(order["product"])
print(total)