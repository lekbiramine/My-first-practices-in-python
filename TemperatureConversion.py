# Temperature Conversion 

# (°C × 9/5) + 32 = °F
# (°F − 32) × 5/9 = °C




unit = input("Is the temperature in (C)elsius or (F)ahrenheit? \n").strip().upper()
temp = float(input("Enter the temperature:"))

if unit == "C" :

    temp = (temp *9/5) + 32
    print(f"The temperature in Fahrenheit is: {temp}°F")
    
elif unit == "F" : 
    temp = (temp - 32) * 5/9
    print(f"The temperature in Celsius is:  {temp}°C")

else : 
    print(f"{unit} is an invalid unit of measurement.")