# Concession Stand Program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50, 
        "chips":1.00,
        "pretzel": 3.50,
        "soda":3.00,
        "lemonade": 4.25} 

cart = []
total = 0

# the menue

print("------- MENU --------")
for key, value in menu.items(): 

    print(f"{key:10}: {value:.2f}DA")
print("----------------------")

# quit + appending the food choice to the cart

while True: 
    food = input("Select an item (q to quit): ").strip().lower()

    if food == "q" or food == "quit": 
        break
    
    elif menu.get(food) is not None: 
        cart.append(food)

    else: 
        print("Your Choice isn't in the menu")

print("---------- YOUR ORDER ---------")
for food in cart: 

    total += menu.get(food)
    print(food, end=" ")

print()
print("---------- YOUR Bill ---------")
print()
print(f"The Total : ${total:.2f}")
print()
print("---------- Bon appétit! ---------")

# So good :)