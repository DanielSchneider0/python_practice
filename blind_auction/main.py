from turtle import clear
from art import logo

print(logo)

new_bid = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for key in bidding_record:
        bid_amount = bidding_record[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not bidding_finished:
    bidder_name = input("What is you name?\n")
    bid_price = int(input("what is your bid price?\n$"))
    new_bid[bidder_name] = bid_price
    yes_continue = input('Are ther any other bidders? Type "Yes" or "No"?\n')
    if yes_continue == "no":
        bidding_finished = True
        highest_bidder(new_bid)
    elif yes_continue == "yes":
        clear()
