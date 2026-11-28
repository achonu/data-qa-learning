order_ids = []

if len(order_ids) == 0:
    print("No records available for duplicate validation")

elif len(order_ids) != len(set(order_ids)):
    print("Duplicate orders found")

else:
    print("No duplicate orders found")


for order_id in set(order_ids):
    if order_ids.count(order_id) >1:
        print(order_id, order_ids.count(order_id), "times")