import static.secret_auction_art
from static import secret_auction_art

print(secret_auction_art.logo)

another_bid = True
bid_tracker = {}
while another_bid:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    bid_tracker[name] = bid

    another_user = input("Is there another bid? (y/n) ").lower()
    another_bid = another_user == "y"
    if another_bid:
        print("\n" * 100)

highest_bid = 0
highest_bidder = ""
for key in bid_tracker:
    if bid_tracker[key] > highest_bid:
        highest_bid = bid_tracker[key]
        highest_bidder = key
print(f"{highest_bidder} won this item with ${highest_bid}! Congrats!")