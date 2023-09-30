from collections import OrderedDict

# Number of items
n = int(input())

# Create an ordered dictionary to store item_name as keys and net_price as values
items_ordered_dict = OrderedDict()

# Iterate through the input and calculate net prices
for _ in range(n):
    item_info = input().split()
    item_name = " ".join(item_info[:-1])  # Join all words except the last as item_name
    price = int(item_info[-1])
    
    # Check if the item_name is already in the ordered dictionary
    if item_name in items_ordered_dict:
        items_ordered_dict[item_name] += price
    else:
        items_ordered_dict[item_name] = price

# Print the item_name and net_price in order of their first occurrence
for item_name, net_price in items_ordered_dict.items():
    print(item_name, net_price)
