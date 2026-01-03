# Random password 
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation

try:
    passlen = int(input("Write the length of the password you want: "))
    if passlen < 0:
        print("Number cannot be less than zero.")
    else:
        password = "".join(random.choice(chars) for _ in range(passlen))
        print(f"Here is your password: {password.strip()}")

except ValueError:
    print("Invalid input (ONLY NUMBERS ALLOWED!)")