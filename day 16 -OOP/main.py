from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()


# item = menu.find_drink("latte")
# if item:
#     print(f"{item.name}, {item.cost}, {item.ingredients}")


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# money_machine.report()
# print(menu.get_items())

def runmachine():
    machine_running = True
    while machine_running == True:
        print("Would you like to order a coffee or print report?")
        coffee_or_report = input("coffee/report/refill/end/ ").lower()
        if coffee_or_report == "report":
            coffee_maker.report()
            money_machine.report()
        elif coffee_or_report == "end":
            machine_running == False
            break
        elif coffee_or_report == "refill":
            coffee_maker.resources["water"] = 300  # Change the water value 
            coffee_maker.resources["milk"] = 200   # Change the milk value 
            coffee_maker.resources["coffee"] = 100  # Change the coffee value 
            print("The machine has been successfully refilled!")
        else:  
            print("What would you like to order?")
            order = input(menu.get_items())
            drink = menu.find_drink(order)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(drink) == True:
                    if money_machine.make_payment(drink.cost):
                        coffee_maker.make_coffee(drink)
            #     else:
            #         pass
            # else:
            #     pass
        


runmachine()