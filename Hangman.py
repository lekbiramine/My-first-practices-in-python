# Hangman game in python

import random

words = ("apple","orange","banana","coconut","pineapple")

# dictionary of key:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
                1: (" o ",
                    "   ",
                    "   "),
                2: (" o ",
                    " | ",
                    "   "),
                 3: (" o ",
                     "/| ",
                     "   "),
                 4: (" o ",
                     "/|\\",
                     "   "),
                 5: (" o ",
                     "/|\\",
                     "/  "),
                 6: (" o ",
                     "/|\\",
                     "/ \\")}

def display_man(wrong_guesses):
     
    print("******************")
    for line in hangman_art[wrong_guesses]:
         print(line)

    print("********************")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main(): 
    answer = random.choice(words) 
    hint = ["_"] * len(answer)
    wrong_guesses = 6
    guessed_letters = set()
    is_running = True 

    while is_running :
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        guessed_letters.add(guess)

        if guess in guessed_letters:
            print(f"{guess} is already guessed")

    
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess: 
                    hint[i] = guess
        
        else : 
            wrong_guesses += 1

        if "_" not in hint: 
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running = False


if __name__ == "__main__":
    main()

# Okay so the next time we will watch the video , then repeat the project ALONE , if we really stuck on it :
# we will search on the net , if we really couldn't find the solution we will comeback to the project
# I don't Understand ! 