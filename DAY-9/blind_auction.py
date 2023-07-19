"""
Project Name:Blind Auction
Project Description: This is a program that compares the bids of auction participants
and determines the highest bidder.
Note:Participants must not see each other's offer
"""
#import click
# from IPython.display import clear_output
# import os

import art

print(art.logo)
print("Welcome to the secret auction program.")
dict = {}
end_code = False
while not end_code:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    dict[name] = bid
    other_bidders = input("Are there other bidders? Type 'yes' or 'no'.\n")
    # Participants must not see each other's offer :
    print('\n' * 80)        #Faking Clear Screen (for PyCharm)
    # Another version to clear the screen on Windows System:
    # def clr_screen():
    #     os.system('cls')
    #     print("screen cleared.")
    # clr_screen()

    #Another version:
    #click.clear()

    # Another version:
    # clear_output(wait=True)

    if other_bidders == "no":
        end_code = True

highest = 0
for key in dict:
    if dict[key] > highest:
        highest = dict[key]
        winner = key

print(f"The winner is {winner} with a bid of ${highest}.")