import random 

num = random.randint(0,100)
num_of_guesses = 0

is_running = True
while is_running:
    choice = int(input("Enter a number between 0 and 100: "))
    if choice > num :
        print("Too high!")
        num_of_guesses += 1
    elif choice < num :
        print("Too low!")
        num_of_guesses += 1
    else:
        print("You guessed the right number!")
        print(num_of_guesses)
        is_running = False
