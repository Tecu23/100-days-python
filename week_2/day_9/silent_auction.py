from os import system

print("Welcome to the secret auction program.")

bidding_finished = False

bidders = []

while not bidding_finished:
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    
    bidders.append({
        "name": name,
        "bid": bid
    })
    
    continue_program = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if continue_program == 'no':
        bidding_finished = True
    else:
        system('clear')

winner = {}
max_amount = float('-Infinity')

for bidder in bidders:
    if bidder["bid"] > max_amount:
        max_amount = bidder["bid"]
        winner = bidder

print(f"The winner is {winner['name']} with a bid of {winner['bid']}")
