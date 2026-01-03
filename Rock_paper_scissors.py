# Rock , Paper, Scissors
import random 
player_wins = 0
computer_wins = 0
choices = ["rock", "paper", "scissors"]
running = True

print("#### You Can write the first letter of your choice (r p s)####".center(60))

while running : 

    player_choice = input("\nEnter your choice : (Rock/paper/scissors) or \"q\" to quit: ").strip().lower()

    if player_choice in ["quit","q"]:
        print("\nGame over!")
        print(f"You: {player_wins} - Computer: {computer_wins}")
        break

    if player_choice == "r":
        player_choice = "rock"
    
    elif player_choice == "p":
        player_choice = "paper"
    
    elif player_choice == "s":
        player_choice = "scissors"

    if player_choice not in choices: 

        print("Invalid choice, try again.")
        continue 

    computer_choice = random.choice(choices) 
    print(f"You chose {player_choice.upper()} - Computer chose {computer_choice.upper()}") 

    if player_choice == computer_choice: 
        print("it's a tie!")

    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        
        print("You won !") 
        player_wins += 1 

    else : 
        print("Computer wins , good luck next time :)")
        computer_wins += 1 
        

    print(f"Score: You: {player_wins} , Computer: {computer_wins}")


    if not input("play again ? (y/n): ").strip().lower() in ["yes", "y"]: 

        running = False
        print("Thanks for playing")




