from ascii_art import logo
from utilities import clear,find_highest_bidder

print(logo)

bids = {}
more_bids = True

print("Welcome to Secret Auction!")
while more_bids:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    more = input("Would you like to add another bid? (y/n) ").lower()
    if more == "n":
        more_bids = False
    clear()

find_highest_bidder(bids)


