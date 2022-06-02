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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. Print report of coffee machine resources


# TODO: 3. get order info from user


# TODO: 2. Turn off coffee machine


# TODO: 3. Check if resources are sufficient to make drink


def check_resources(drink_ingredients):
    for key in drink_ingredients:
        if drink_ingredients[key] > resources[key]:
            print(f"Not enough ingredients to make your coffee.")
            return False
        else:
            return True


def process_payment():
    total_payment = int(input("How many quarters?")) * 0.25
    total_payment += int(input("How many dimes?")) * 0.1
    total_payment += int(input("How many nickels?")) * 0.05
    total_payment += int(input("How many pennies?")) * 0.01
    print(f"Your payment is ${total_payment}")
    return total_payment


def transaction_successful(money, drink_cost):
    if money >= drink_cost:
        print("payment successful")
        return True
    else:
        print("Not enough money inserted for the drink")
        return False


def make_coffee(coffee_selected, drink_ingredients):
    for key in drink_ingredients:
        resources[key] -= drink_ingredients[key]
    print(f"Here is you {coffee_selected}")


is_on = True
while is_on:
    order = input("What would you like? (espresso, latte, cappuccino): ").lower()
    if order == "off":
        is_on = False
    elif order == "report":
        print(resources)
    else:
        coffee = MENU[order]
        if check_resources(coffee["ingredients"]):
            payment = process_payment()
            if transaction_successful(payment, coffee["cost"]):
                make_coffee(order, coffee["ingredients"])
