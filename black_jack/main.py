import random

from click import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(player_score, dealer_score):
    if player_score == dealer_score:
        return "Draw"
    elif dealer_score == 0:
        return "Loss, Dealer has blackjack"
    elif player_score == 0:
        return "Winner, Blackjack"
    elif player_score > 21:
        return "Player Bust"
    elif dealer_score > 21:
        return "Winner. Dealer Bust"
    elif player_score > dealer_score:
        return "You win."
    else:
        return "You lose."


def play():
    print(logo)
    player = []
    dealer = []
    game_over = False

    for _ in range(2):
        player.append(deal_card())
        dealer.append(deal_card())
    while not game_over:
        player_score = calculate_score(player)
        dealer_score = calculate_score(dealer)
        print(f"Player's cards: {player}, Player's score: {player_score}")
        print(f" Dealer's card: {dealer[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            hit = input("Type 'y' to hit, type 'n' to pass: ")
            if hit == "y":
                player.append(deal_card())
            else:
                game_over = True

    while dealer != 0 and dealer_score < 17:
        dealer.append(deal_card())
        dealer_score = calculate_score(dealer)

    print(f"Your final hand is {player}, final score {player_score}")
    print(f"Dealer final hand: {dealer}, final score {dealer_score}")

    print(compare(player_score, dealer_score))


while input("play blackjack? 'y' or 'n'") == "y":
    clear()
    play()
