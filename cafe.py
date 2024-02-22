import math

# cafe menu
menu = ["latte", "tea", "hot chocolate", "sandwich"]

# stock value for each menu item
stock = {
    "latte" : 40,
    "tea" : 50,
    "hot chocolate" : 35,
    "sandwich" : 25
}
# item prices
price = {
    "latte" : 2.15,
    "tea" : 1.50,
    "hot chocolate" : 3.20,
    "sandwich" : 4.00
}

# getting the value and price for each item in the menu and adding it to a list
totals_list = []
for item in menu:
    value = stock[item]
    worth = price[item]
    total = value * worth
    totals_list.append(total)

# adding up the total for all items
total_worth = math.fsum(totals_list)
print(f"The total worth of my 'Hello Cat Cafe' is {total_worth}! <3")