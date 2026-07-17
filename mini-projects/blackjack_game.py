"""The objective of Blackjack, also known as Twenty-One, is to beat the dealer by getting a hand value closer to 21
than the dealer’s hand, without going over 21. """

#todo need to make the 11 card a 1 when the user_deck and dealer_deck is over 21 points
import random
import static.logos

user_score = 0
dealer_score = 0
user_deck = []
dealer_deck = []
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def calculate_starting_score(hand):
    return sum(hand)

wanna_play_answer = input("Do you want to play BlackJack? (y/n) ").lower()
wanna_play = (wanna_play_answer == "y")
game_round = 1
while wanna_play:
    if game_round == 1:
        print(static.logos.blackjack_logo)
        print("Welcome to BlackJack! I will now deal the cards.")
        # each user will get two cards to start
        user_deck.append(random.choice(cards))
        user_deck.append(random.choice(cards))
        dealer_deck.append(random.choice(cards))
        dealer_deck.append(random.choice(cards))
        # if the dealer has less than 17 points we must deal a new card
        user_score += calculate_starting_score(user_deck)
        dealer_score += calculate_starting_score(dealer_deck)
        if dealer_score < 17:
            dealer_deck.append(random.choice(cards))
            dealer_score += dealer_deck[2]
        print(f"You have these cards: {user_deck}")
        print(f"Here is the dealer's first card: {dealer_deck[0]}")

    hit_me = input("Do you want to call it or get another card? n for calling it and y for another card (y/n) ").lower()
    if hit_me == "y":
        game_round += 1
        user_deck.append(random.choice(cards))
        user_score += user_deck[len(user_deck) - 1]
        print(f"You have these cards: {user_deck}")
        print(f"Here is the dealer's first card: {dealer_deck[0]}")
    else:
        game_round = 1
        if user_score > 21:
            print("You lose!")
        elif dealer_score > 21:
            print("You win!")
        elif dealer_score == user_score:
            print("It's a draw!")
        elif user_score > dealer_score:
            print("You win!")
        else:
            print("You lose!")
        wanna_play_answer = input("Do you want to play again? (y/n)").lower()
        wanna_play = (wanna_play_answer == "y")
        if wanna_play:
            user_score = 0
            dealer_score = 0
            user_deck = []
            dealer_deck = []
print("Goodbye, please come play again!")