'''
Create a dictionary called shopping_cart
The dictionary will contain mappings of items for an online store
The items will have the item name as the key and then the corresponding quantity and price as value. I.e, sneakers is
the name of the item, and 1, 120 as the corresponding quantity and price
The dictionary should have at least 5 items. More is fine.
Display all the keys in the dictionary
Display all the values in the dictionary
Iterate over the dictionary and display the key/ value pairs
Create a new dictionary called sale and only add items from the sopping_cart dictionary that are <= $10. If there's no
items that's less than $10, then update the dictionary with two items that are <= $10 :wink:
Print the sale dictionary
'''

import collections
shopping_cart = {'python book': [10, 35],
                 'keyboard': [200, 8],
                 'mouse': [50, 5],
                 'laptop': [50, 400],
                 'monitor': [25, 100],
                 'printer':[30, 9]
}
# creating empty dictionary for sale items
sale_items = {}

# display keys of the shopping cart
print("Items available online:", shopping_cart.keys())

# display values of the shopping cart
print("\nQuantity and Price for the each item:", shopping_cart.values())

#display the shopping_cart dictionary
print()
'''
< will indicate left aligned
> will indicate right aligned
^ will indicate center aligned
Reference:
http://zetcode.com/python/fstring/
https://stackoverflow.com/questions/8450472/how-to-print-a-string-in-fixed-width
'''
Row1 = "Item"
Row2 = "Number of Quantity"
Row3 = "Price per item"

print(f"{Row1:<20}{Row2:<20}{Row3}")
for key, val in shopping_cart.items():
    print(f"{key:<20}{val[0]:<20}{val[1]}")
    if val[1] <= 10:
        sale_items.update({key: val})

print()
print(20*"*" + " Items for sale " + 20*"*")
print(f"{Row1:<20}{Row2:<20}{Row3}")
for key, val in sale_items.items():
    print(f"{key:<20}{val[0]:<20}{val[1]}")