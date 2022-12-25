from art import logo
from os import system
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

system("clear")
print(logo)

def encrypt(user_input,shift):
	encrypted_msg = ""
	for letter in user_input:
		if(letter.isalpha()):
			encrypted_msg+=alphabets[(alphabets.index(letter)+shift)%26]
		else:
			encrypted_msg+=letter
	print(encrypted_msg)

def decrypt(user_input,shift):
	decrypted_message = ""
	for letter in user_input:
		if(letter.isalpha()):
			decrypted_message+=alphabets[(alphabets.index(letter)-shift)]
		else:
			decrypted_message+=letter
	print(decrypted_message)

while True:
	user_choice = (input('Type "encode" to encrypt, type "decode" to decrypt:\n'))
	if(user_choice=="encode"):
		user_input = input("Enter a message to encrypt: ")
		shift = int(input("Enter the shift value: "))
		encrypt(user_input,shift)

	if(user_choice=="decode"):
		user_input = input("Enter a message to decrypt: ")
		shift = int(input("Enter the shift value: "))
		decrypt(user_input,shift)
	user_choice = input("Do you want to continue? ")
	if(user_choice!="yes"):
		break