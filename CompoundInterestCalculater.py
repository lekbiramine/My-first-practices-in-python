# Python compound Interest calaculator 

# A = P*(1+ r/n)**t

# A = Final Amount
# P = Initial principal blanace 
# r = interest rate 
# t = number of time periods elapsed 

principle = 0
rate = 0
time = 0

while principle <= 0 : 
    principle = float(input("Enter The principle amount :"))

    if principle <= 0 : 
        print("principle can't be less than or equal to zero")


while rate <= 0 : 
    rate = float(input("Enter The interest rate :"))

    if rate <= 0 : 
        print("iterest rate can't be less than or equal to zero")


while time <= 0 : 
    time = int(input("Enter The time in years :"))

    if time <= 0 : 
        print("iterest time can't be less than or equal to zero")

total = principle * pow((1 + rate / 100 ), time)
print(f"Balance after {time} year/s: ${total:.2f}")



# if you use while True : , you need to do : else : break , or the loop will continue forever