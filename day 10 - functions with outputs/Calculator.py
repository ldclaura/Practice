#make sure folder is open to import the logo
from art import logo
print(logo)

def calc():
    result = ""
    number = int(input("What's the first number?: "))
    operation = input("""
+
-
*
/
Pick an operation: 
""")
    next_number = int(input("What's the next number?: "))
    if operation == "+":
        result = number + next_number
        print(result) #return not working
    elif operation == "-":
        result = number - next_number
        print(result)
    elif operation == "*":
        result = number * next_number
        print(result)
    elif operation == "/":
        result = number / next_number
        print(result)
    else:
        print("not an option")
    if_continue = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
    lowercase_continue = if_continue.lower()

    if lowercase_continue == "y":
        print(f"Your first number is {result}")
        operation = input("""
+
-
*
/
Pick an operation: 
""")
        next_number = int(input("What's the next number?: "))
        if operation == "+":
            result = result + next_number
            print(result) #return not working
        elif operation == "-":
            result = result - next_number
            print(result)
        elif operation == "*":
            result = result * next_number
            print(result)
        elif operation == "/":
            result = result / next_number
            print(result)
        else:
            print("not an option")


    elif lowercase_continue == "n":
        calc()
#n is supposed to clear the screen but i don't care.
    
#ANGELAS SOLUTION NOTES:

#def add(n1, n2):
    #return n1 + n2

#def subtract yadaydadya

#def multiply

#def divide

#-------------------------------------
#NOTE create a dictionary named operations
#  that takes the operation as key and values 
# are named of functions
#-----------------------------------

#operations = {
# "+": add,
# "-": subtract
# "*": multiply
# "/": divide
#}

#num1 = int(input("What's the first number?: "))

#NOTE work on for loops
#NOTE work on return statements
#for symbol in operations:
#   print(symbol)
#operation_symbol = input("pick an operation from the line above: ")
#num2 = int(input("What's the second number?: "))
#calculation_function = operations[operation_symbol]
# answer = calculation_function(num1, num2)


