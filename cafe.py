# list of items sold in the business

menu = ["donut", "latte", "breakfast bun", "juice"]

# dictionary storing stock value for items
stock = {"donut": 2000,
         "latte": 3000,
         "breakfast bun": 5000,
         "juice": 10000,
         }

# dictionary storing price for items
price = {"donut": 50.5,
         "latte": 75.5,
         "breakfast bun": 125.5,
         "juice": 65.5}

# variable to store total cost of all stock
total_stock = 0

# loop all items in the menu
for item in menu:
    # calculate value of current item stock
    item_value = stock[item] * price[item]
    # add to total
    total_stock += item_value

# print thr total stock worth
print(f"Total stock worth: R{total_stock}")