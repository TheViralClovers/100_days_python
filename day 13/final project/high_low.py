from art import logo,vs
from random import choice
from data import data
from os import system

def get_celebs_info(celeb_1="empty"):
	if celeb_1=="empty":
		celeb_1 = choice(data)
	celeb_2 = choice(data)
	while(celeb_1!=celeb_2):
		celeb_2= choice(data)
	return celeb_1,celeb_2

def display_data(celeb_1,celeb_2):
	print(f"Compare A: {celeb_1['name']}, a {celeb_1['description']}, from {celeb_1['country']}.")
	print(vs)
	print(f"Against B: {celeb_2['name']}, a {celeb_2['description']}, from {celeb_2['country']}.")

def check_answer(guess,celeb_1,celeb_2):
	if(celeb_1['follower_count']>celeb_2['follower_count']):
		return guess=='a'
	return guess=='b'

continue_condition = True
celeb_1,celeb_2 = get_celebs_info()
user_score = 0

while(continue_condition):
	display_data(celeb_1,celeb_2)
	user_choice =  input("Who has more follower_count? Type 'A' or 'B': ").lower()
	hasGuessedCorrectly = check_answer(user_choice,celeb_1,celeb_2)
	system("cls")
	print(logo)
	if(hasGuessedCorrectly):
		user_score+=1
		print(f"You're right! Current score {user_score}.")
		celeb_1,celeb_2 = get_celebs_info(celeb_1)
	else:
		print(f"Sorry that's wrong. Final Score: {user_score}")
		continue_condition = False
