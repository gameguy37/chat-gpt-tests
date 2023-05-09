"""
1. create a program in python that allows a human player to play blackjack against a computer opponent (the dealer)
using a standard 52-card playing deck

2. modify the existing code so that the dealer's hand is shown to the player also when the player is prompted to
either hit or stand. Do not reveal the dealer's hidden card during this stage, but do show the human player the
dealer's face-up card

3. this code does not work because it results in an IndexError when trying to display the dealer's hand.

4. this code still does not work properly. It does not generate an error anymore, but the Dealer's Hand is displayed
to the player incorrectly. It only shows the words "Hidden Card" when it should show the face-up Dealer card
as well as the Hidden Card

5. this new version of the program works for the most part. However, now when the game is over and the result is a
Dealer bust, the dealer's Hidden card is not shown to the player. The Hidden Card should not be shown to the player
during requests for input (hit or stand), but should be shown at the end of the game

6. this did not fix the issue. the problem has reappeared where the Dealer's face-up card is not shown to the player
during requests for input. The Dealer's face-up card needs to be displayed to the player throughout the game when
requesting user input and then, at the end of the game (no matter the result), all the Dealer's cards should
become visible to the player so that the result can be understood

7. this is still not working. The dealer's hand is incorrectly being reported as 'Hidden Card' during request for
user input when it should, instead, be reported as 2 different cards (a face-up card and a Hidden Card).
Only at the end of the game should the Dealer's Hidden card be revealed to the player
"""

import random


def create_deck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['♠', '♣', '♥', '♦']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck


def get_card_value(card):
    rank = card[0]
    if rank in ['J', 'Q', 'K']:
        return 10
    elif rank == 'A':
        return 11
    else:
        return int(rank)


def calculate_hand_value(hand):
    value = sum(get_card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card[0] == 'A')

    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value


def print_hand(hand, hidden=False, end_game=False):
    if hidden and not end_game:
        print(hand[0])  # Show the face-up card only
        print("Hidden Card")
    else:
        for card in hand:
            print(card)


def play_blackjack():
    deck = create_deck()
    player_hand = []
    dealer_hand = []

    # Initial deal
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())
    player_hand.append(deck.pop())
    dealer_hand.append(deck.pop())

    # Player's turn
    while True:
        print("\nPlayer's Hand:")
        print_hand(player_hand)

        print("\nDealer's Hand:")
        print_hand(dealer_hand, hidden=True)

        player_hand_value = calculate_hand_value(player_hand)
        if player_hand_value == 21:
            print("Blackjack! Player wins!")
            return
        elif player_hand_value > 21:
            print("Player busts! Dealer wins!")
            return

        choice = input("Do you want to hit or stand? (h/s): ").lower()
        if choice == 'h':
            player_hand.append(deck.pop())
        elif choice == 's':
            break

    # Dealer's turn
    print("\nDealer's Hand:")
    print_hand(dealer_hand)

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    dealer_hand_value = calculate_hand_value(dealer_hand)
    if dealer_hand_value > 21:
        print("Dealer busts! Player wins!")
    elif dealer_hand_value > calculate_hand_value(player_hand):
        print("Dealer wins!")
    elif dealer_hand_value < calculate_hand_value(player_hand):
        print("Player wins!")
    else:
        print("It's a tie!")

    # Show all dealer's cards at the end
    print("\nFinal Dealer's Hand:")
    print_hand(dealer_hand, end_game=True)


play_blackjack()
