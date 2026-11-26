expected_rejected_ids = [802, 803]
actual_rejected_ids = [803, 802]
unexpected_rejected_ids = set(actual_rejected_ids) - set(expected_rejected_ids)

missing_rejected_ids = set(expected_rejected_ids) - set(actual_rejected_ids)


if sorted(expected_rejected_ids) == sorted(actual_rejected_ids):
    print("Record reconciliation passed")

else:
    print("Record reconciliation failed:")


print("Unexpectedly rejected orders:",unexpected_rejected_ids)
print("Missing rejected orders:",missing_rejected_ids)