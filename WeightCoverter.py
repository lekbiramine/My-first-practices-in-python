# Weight Converter 

weight = float(input("Enter the weight : \n"))
unit = input("Kilograms or Pounds (K/L) ? \n")

if unit.upper().strip() == "K":

    weight *= 2.205
    unit = "Lbs"
    print(f"The weight is : {round(weight, 2)} {unit}")

elif unit.upper().strip() == "L": 
    weight /= 2.205 
    unit = "Kgs"
    print(f"The weight is : {round(weight, 2)} {unit}")


else : 
    print(f"{unit} is not a valid unit")

