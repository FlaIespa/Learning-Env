from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)

print("Welome to the secret auction program.")

name = input("What is your name?")
bid = input("What is your bid?")
bidders = input("Are there any other bidders? Type yes or no.")

bids_all = [bid]

while bidders == "yes":
  clear()
  name = input("What is your name?")
  bid_others = input("What is your bid?")
  bidders = input("Are there any other bidders? Type yes or no.")
  
bids_all.append(bid_others)

print(f"The winner is: {max(bids_all)}")

# Course Solution
from art import logo
print(logo)

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  # {"Angela: 123"; "James: 321"}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      wiinner = bidder
  print("The winner is {winner} wwith a bid of ${highest_bid}.")
  
while not bidding_finished:
  name = input("What is your name?: ")
  price = int(input("What is your bid?: "))
  bids[name] = price
  should_continue = input('Are there any other bidders? Type yes or no.')
  if should_continue == "no":
    bidding_finished = True
  elif should_continue == "yes":
    clear()

# My solution with dictionary
'''
from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art
print(art.logo)
print("Welome to the secret auction program.")

name = input("What is your name?")
bid = input("What is your bid?")
bidders = input("Are there any other bidders? Type yes or no.")

bid_information = [{
  "name": name,
  "bid": bid
}]

while bidders == "yes":
  clear()
  name = input("What is your name?")
  bid_others = input("What is your bid?")
  bidders = input("Are there any other bidders? Type yes or no.")

  other_bidders = {
    "name": name, 
    "bid": bid_others
  }
  
  bid_information.append(other_bidders)

print(f"The winner is: {max(bid_information)}")

 '''