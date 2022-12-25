from art import logo
from os import system
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

def caesar(user_input,shift,direction):
	final_message = ""
	if(direction=="decode"):
		shift*=-1
	for letter in user_input:
		if(letter.isalpha()):
			final_message+=alphabets[(alphabets.index(letter)+shift)%26]
		else:
			final_message+=letter
	print(final_message)

while True:
	user_choice = (input('Type "encode" to encrypt, type "decode" to decrypt:\n'))
	user_input = input("Enter the message: ")
	shift = int(input("Enter the shift value: "))
	caesar(user_input,shift,user_choice)
	user_choice = input("Do you want to continue? ")
	if(user_choice!="yes"):
		break