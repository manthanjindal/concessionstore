menu = {"pizza":3.00,"nachos":4.50,"popcorn": 6.00,"fries": 2.50,"chips": 1.00,"pretzel":3.50,"soda": 3.00,"lemonade": 4.25}

def print_menu():
    for key,value in menu.items():
        print(f"{key:10} : {value:.2f}")

def get_order():
    cart = []
    total = 0
    print("What would you like to order? ", end = ' ')
    while True:
        item = input()
        if 'no' in item or 'na' in item:
            break
        if item not in menu.keys():
            print("we dont serve that")
        else:
            cart.append(item)
            total += menu[item]
        print("is there anything else you'd like to order? ", end = '')

    return cart,total
        
def main():
    print_menu()

    cart, total = get_order()
    print(f"\nthank you for shopping at the mj consession store\n\n-------------------------------\n\tYour total is ${total}/- \n-------------------------------\n")


main()