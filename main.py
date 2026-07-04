menu = {"pizza":3.00,"nachos":4.50,"popcorn": 6.00,"fries": 2.50,"chips": 1.00,"pretzel":3.50,"soda": 3.00,"lemonade": 4.25}

cart = []
total = 0

for key in menu.keys():
    print(f"{key} : {menu[key]}")

print("What would you like to order")
while True:
    item = input()
    print("is there anything else you'd like to order?")
    print("(press '67' to exit)")
    if item == '67':
        print(f"thank you for shopping at the mj consession store\nYour total is {total}")
        break
    if item not in menu.keys():
        print("we dont serve that")
    else:
        cart.append(item)
        total += menu[item]
    


    
