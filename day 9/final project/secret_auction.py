from art import logo
from os import system
bidders_dict = {}

def add_bidder(bidders_name,bid_amount):
	bidders_dict[bidders_name]=bid_amount

def check_winner():
	max_bidder_name = ""
	max_bid = 0
	for bidder in bidders_dict:
		if(bidders_dict[bidder]>max_bid):
			max_bid = bidders_dict[bidder]
			max_bidder_name = bidder
	return ([max_bidder_name,max_bid])


print(logo)
print("Welcome to the secret auction program.")

while(1):
	bidders_name = input("What is your name?: ")
	bid_amount = int(input("What's your bid?: $"))
	add_bidder(bidders_name,bid_amount)
	other_bidders_check = input("Are there any other bidders? Type 'yes' or 'no': ")
	if(other_bidders_check == "no"):
		max_bidder_name,max_bid = check_winner()
		print(f"The winner is {max_bidder_name} with a bid of ${max_bid}")
		break
	else:
		system("cls")