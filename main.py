menu = {"pizza":3.00,"nachos":4.50,"popcorn": 6.00,"fries": 2.50,"chips": 1.00,"pretzel":3.50,"soda": 3.00,"lemonade": 4.25}

cart = []
total = 0

for key,value in menu.items():
    print(f"{key:10} : {value:.2f}")

print("What would you like to order")
while True:
    item = input()
    print("is there anything else you'd like to order?")
    if 'no' in item or 'na' in item:
        print(f"\nthank you for shopping at the mj consession store\n\n-------------------------------\n\tYour total is ${total}/- \n-------------------------------\n")
        break
    if item not in menu.keys():
        print("we dont serve that")
    else:
        cart.append(item)
        total += menu[item]
    


    
