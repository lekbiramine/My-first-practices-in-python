# trying to make membership program


# Admins list
admins = ["Anes","Mohamed","Ishak","Doliprane"]

# Login info 
user = input("Your name please: ").strip().capitalize()

if user in admins :

    print(f"Hello {user} you are admin !")

    choice = input("Do you want to change or Delete your name ? (y/n) ").strip().lower()

    if choice == 'yes' or choice == 'y' :

        choice02 = input("Delete or Edit ? (D /E) ").strip().capitalize() 

        if choice02 == 'Delete' or choice02 == 'D' :

            admins.remove(user)

            print("Your Name Have Been Deleted Successfully !")

            print(admins)

        elif choice02 == 'Edit' or choice02 == 'E' :

            theNewName = input("Enter The New Name Please: ").strip().capitalize()

            admins[admins.index(user)] = theNewName

            print("Your name have been changed successfully !")

            print(admins) 
        
        else : 

            print("Invalid input(\"Delete\" \\\"Edit\")")

    elif choice == 'no' or choice == 'n' :

        print("Okay You will stay an admin :)")

    else :

        print("invalid input(y/n)")
        
else : 

    print("You are not an admin")

