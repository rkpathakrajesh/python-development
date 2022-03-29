shoping_list =["Milk", "pasta", "eggs", "spam","bread","rice"]

# for item in shoping_list:
#     if item != "spam":
#         print("Buy " + item)

for item in shoping_list:
    if item =="spam":
        continue
    print("Buy " + item)