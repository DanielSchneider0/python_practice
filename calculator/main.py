from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


dictionary = {"/": divide, "*": multiply, "-": subtract, "+": add}


def calculator():
    num1 = float(input("What is the first number?\n"))
    for key in dictionary:
        print(key)

    proceed = True
    while proceed:
        dictionary_symbol = input("Pick and operation from above: ")
        num2 = float(input("What is the second number?\n"))
        calc_fuction = dictionary[dictionary_symbol]
        first_answer = calc_fuction(num1, num2)

        print(f"{num1} {dictionary_symbol} {num2} = {first_answer}")

        result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
        if result == "yes":
            num1 = first_answer
        elif result == "no":
            proceed == False
            calculator()


calculator()
