#main.py
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



#requirements
#print report (resources left)
#check resources sufficient?
#process coins
#check transaction successful
#make coffee


def check_resources(water_milk_or_coffee):
    """ Checks resources returns resources """
    value_of_ = resources.get(water_milk_or_coffee)
    return value_of_

report_resources_water = check_resources("water")
report_resources_milk = check_resources("milk")
report_resources_coffee = check_resources("coffee")


def print_report(water, milk, coffee):
    """ Prints a report based on check_resources """
    values = f"The value of water is {water}, the value of milk is {milk}, the value of coffee is {coffee}"
    return values

def process_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?")) * 25
    dimes = int(input("How many dimes?")) * 10
    nickels = int(input("How many nickels?")) * 5
    pennies = int(input("How many pennies?"))
    #print(f"pennies - {pennies}, nickels - {nickels}, dimes - {dimes}, quarters - {quarters}")
    money = (quarters + dimes + nickels + pennies) / 100
    print(f"You have put in ${money}")
    check_transaction(coffee_type, money)
    #coin operate
#penny, nickel, dime, quarter.
#penny = 1 cent
#nickel = 5 cents
#dime = 10 cents
#quarter = 25 cents
    
    #Please insert coins. \n How many quarters?: 
#How many dimes?
#How many nickels?
#How many pennies?

def check_transaction(coffee_type, cost):
    """ Checks if you have enough money 

    
    https://stackoverflow.com/questions/43752962/how-to-iterate-through-a-nested-dict"""
    make_the_coffee = False
    if coffee_type == "latte":
        if cost > 2.5:
            the_return = cost - 2.5
            print(f"You have been returned ${the_return}")
            make_the_coffee = True
        elif cost == 2.5:
            make_the_coffee = True
        else:
            print("You do not have enough")
            run_machine()
    elif coffee_type == "espresso":
        if cost > 1.5:
            the_return = cost - 1.5
            print(f"You have been returned ${the_return}")
            make_the_coffee = True
        elif cost == 1.5:
            make_the_coffee = True
        else:
            print("You do not have enough")
            run_machine()
    else:
        if cost > 3.0:
            the_return = cost - 3.0
            print(f"You have been returned ${the_return}")
            make_the_coffee = True
        elif cost == 3.0:
            make_the_coffee = True
        else:
            print("You do not have enough")
            run_machine()
    if make_the_coffee == True:
        make_coffee(coffee_type)



def make_coffee(the_coffee_type):
    water_used = MENU[the_coffee_type]["ingredients"]["water"]
    coffee_used = MENU[the_coffee_type]["ingredients"]["coffee"]
    if the_coffee_type != "espresso":
        milk_used = MENU[the_coffee_type]["ingredients"]["milk"]
    else:
        milk_used = 0
    resources["water"] -= water_used
    resources["coffee"] -= coffee_used
    resources["milk"] -= milk_used
    print(f"Here is your {the_coffee_type}!")
    print(resources["water"])
    the_new_resources = new_resources(resources["water"], resources["milk"], resources["coffee"])
    return the_new_resources

    #return resources["water"] - water_used, resources["milk"] - milk_used, resources["coffee"] - coffee_used

def new_resources(the_water, the_milk, the_coffee):
    resources.update({
    "water": the_water,
    "milk": the_milk,
    "coffee": the_coffee,
    })
    return resources, run_machine()
#https://stackoverflow.com/questions/65306669/why-does-my-dictionary-doesnt-get-updated-outside-of-the-function-python
#NOTE
#NOTE
#NOTE
#NOTE

def coffee_machine(coffee):
    print(f"You would like to order a {coffee}?")
    if coffee == "espresso":
        print("That will be 1.5")
        process_coins(coffee)
    elif coffee == "latte":
        print("That will be 2.5")
        process_coins(coffee)
    elif coffee == "cappuccino":
        print("That will be 3.0")
        process_coins(coffee)
def run_machine():
    """ The outputs and inputs. Runs the machine."""
    the_input = input("What would you like? (espresso/latte/cappuccino/print report)")
    if the_input == "print report":
        print(report)
    elif the_input in ["espresso", "latte", "cappuccino"]:
        coffee_machine(the_input)
    else:
        print("That is not an option")
        run_machine()



report = print_report(report_resources_water, report_resources_milk, report_resources_coffee)

run_machine()


#What would you like? (espresso/latte/cappuccino): 
#type report - prints how much resources left including how much money it has from u giving it
#type coffee flavour,
#Please insert coins. \n How many quarters?: 
#How many dimes?
#How many nickels?
#How many pennies?
#Here is ___ in change (or) Sorry that's not enough money. Money refunded.
#Here is your (coffee) enjoy!
#What would you like? (repeats)