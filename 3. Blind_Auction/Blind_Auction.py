import Art
import os

print(Art.logo)
print("welcome to secret Auction program.")

shouldGo = False
bids = {}

listed_record = []


def find_highest_bid(records):
    highest_bid = 0
    for bidder in records:
        current_bid = records[bidder]
        if current_bid > highest_bid:
            highest_bid = current_bid
            winner = bidder
    print(f"The winner is {winner} with the highest bid of ${highest_bid}.")


while not shouldGo:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    print("Are there any other bidders? Type 'yes' or 'no'.")
    answer = input()
    if answer == "yes":
        os.system('cls')
        shouldGo = False
    else:
        shouldGo = True
        os.system('cls')
        find_highest_bid(bids)
