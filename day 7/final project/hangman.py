from random import choice
import os

HANGMANPICS = ['''

  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       ''','''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()

def start():
	lives = 7
	raw_word = choice(words)
	letter_board = list(len(raw_word)*"_")
	letter_list = []
	for letter in raw_word:
			if letter not in letter_list:
				letter_list+=letter
	return [lives,raw_word,letter_board,letter_list]

def print_game(lives):
	os.system("cls")
	print(HANGMANPICS[7-lives])
	for letter in letter_board:
		print(f"{letter}",end=" ")

def check_letter(user_letter,lives):
	if user_letter in letter_list:
		letter_list.remove(user_letter)
		for i in range(len(raw_word)):
			if raw_word[i]==user_letter:
				letter_board[i]=user_letter
		return lives
	else:
		return lives-1

def check_win():
	win_condition = 1
	for char in letter_board:
		if char=="_":
			win_condition=0
	return win_condition

while True:
	lives,raw_word,letter_board,letter_list = start()
	while lives:
		print_game(lives)
		user_letter = input("\nGuess a letter: ")
		lives = check_letter(user_letter,lives)
		if(check_win()):
			print_game(lives)
			print("\nYou won")
			break
	if(not lives):
		print_game(lives)
		print("\nYou lose!")
	if(input("Do you want to continue? yes or no ")!="yes"):
		print("Thank you for playing!")
		break