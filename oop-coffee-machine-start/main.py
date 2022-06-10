from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
money = MoneyMachine()
menu = Menu()
coffee_machine_on = True

while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            print(f"{drink.name} is ${drink.cost}.")
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)
    elif choice == "report":
        coffee.report()
        money.report()
    elif choice == "off":
        print("Goodbye")
        coffee_machine_on = False
    else:
        print("Invalid choice")
