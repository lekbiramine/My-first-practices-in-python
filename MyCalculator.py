# building a calculator with python 
operator = input ("Select the Operator please \"+  -  *  /\" \n")
num1_input = input("Enter The First Number \n")
num2_input = input("Enter The Second number \n")

if num1_input.isdigit() and num2_input.isdigit() :
    num1 = int(num1_input)
    num2 = int(num2_input)

    if operator == "+" : 
        result = num1 + num2
        print(f"the result is \" {result} \"" )

    elif operator == "-" : 
        result = num1 - num2
        print(f"the result is \" {result} \"" )

    elif operator == "*" : 
        result = num1 * num2
        print(f"the result is \" {result} \"" )

    elif operator == "/" : 
        result = num1 / num2

        if num2 == 0: 
            print("Division by zero is not allowed")
        else : 
            print(f"the result is \" {result} \"" )

    else : 
        print("invalid operator")

else : 
    print("Only int allowed")

    


    