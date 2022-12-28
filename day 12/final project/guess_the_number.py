from random import randint
from art import logo

print(logo)
print("Welcome to the number guessing game")
print("I'm thinking of a number between 1-100")
game_mode = input("Choose a difficulty type 'easy or 'hard': ")

if(game_mode=='easy'):
	no_of_attempts = 10
else:
	no_of_attempts = 5

hasGuessed = False
random_integer = randint(1,101)

for i in range(no_of_attempts):
	print(f"You have {no_of_attempts-i} attempts remaining to guess the number")
	user_guess  = int(input("Enter your guess: "))
	if(user_guess == random_integer):
		hasGuessed = True
		break
	elif(user_guess>random_integer):
		print("Too high")
	else:
		print("Too low")
	if(no_of_attempts-i):
		print("Guess again.")

if(hasGuessed):
	print(f"You got it! The answer was {random_integer}")
else:
	print("You have run out of guesses, you lose")