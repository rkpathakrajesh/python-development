shoping_list =["Milk", "pasta", "eggs", "spam","bread","rice"]

item_to_find = "albatross"
found_at = None

for index in range(len(shoping_list)):
    if shoping_list[index] == item_to_find:
        found_at=index
        break

if found_at is not None:
    print("Item found at poxition: {}".format(found_at))
else:
    print("{} not found".format(item_to_find))