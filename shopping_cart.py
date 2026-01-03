# Shoping Cart Program

foods = []
prices = []
total = 0

while True : 
    food = input("Enter a food to buy (q to quit): ").lower().strip()
    if food in ["q","quit"]:
        break
    else : 
        price = float(input(f"Enter The price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods: 
    print(f"{food}", end= " ") 

for price in prices : 
    total += price

print()
print(f"Total price is : ${total}")