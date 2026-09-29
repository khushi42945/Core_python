def process_batch_orders(inventory, batch_requests):
    fulfilled_count = 0
    unfulfilled_count = 0

    for item, quantity in batch_requests:
        if item in inventory and inventory[item] >= quantity:
            inventory[item] -= quantity
            fulfilled_count += 1                     
        else:
            unfulfilled_count += 1      

    return inventory, fulfilled_count, unfulfilled_count

godown_stock = {
    "item_a": 10,
    "item_b": 5,
    "item_c": 20
}
orders = [
    ("item_a", 5),
    ("item_b", 12),
    ("item_d", 3),
    ("item_c", 20)
]

updated_stock, passed, failed = process_batch_orders(godown_stock, orders)

print(f"Updated Inventory: {updated_stock}")
print(f"Total Fulfilled: {passed}")
print(f"Total Rejected: {failed}")