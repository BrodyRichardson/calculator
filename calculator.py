#Calculator
#Brody Richardson



def user_i():   #Defines the user input as a choice.
    print("+ for addition")
    print("- for subtraction")
    print("* for multiplication")
    print("/ for division")
    choice = input("Enter operator:")
    
    while choice not in ["+", "-", "*", "/"]:   #If the user types a value other than the ones provided, the while loop runs the program until parameters have been met.
        print("Please enter a value above.")
        print("+ for addition")
        print("- for subtraction")
        print("* for multiplication")
        print("/ for division")
        choice = input("Enter operator:") 
        
    values(choice)

def values(choice):
    num_1 = int(input("Enter your first number: "))
    num_2 = int(input("Enter your second number: "))

    if choice == "+":   #If user inputs +, program adds first entry to second entry.
        print("{} + {} = ".format(num_1, num_2))
        print(num_1 + num_2)
    elif choice == "-":   #If user inputs -, program subtracts first entry from their second.
        print("{} - {} = ".format(num_1, num_2))
        print(num_1 - num_2)
    elif choice == "*":   #If user inputs *, multiplies their first entry by their second.
        print("{} * {} = ".format(num_1, num_2))
        print(num_1 * num_2)
    elif choice == "/":   #If user inputs /, divides their first entry by their second.
        print("{} / {} = ".format(num_1, num_2))
        print(num_1 / num_2)
    


user_i()   #Calls user function