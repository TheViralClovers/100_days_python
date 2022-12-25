from random import randint,choice

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

nr_dict = {"nr_letters":nr_letters,"nr_numbers":nr_numbers,"nr_symbols":nr_symbols}
password=""

for i in range(nr_letters+nr_numbers+nr_symbols):
	try: #throws error when key is popped
		if(not (nr_dict["nr_letters"])): #remove a requirement from a list once it reaches 0
			nr_dict.pop("nr_letters")
			# print("removed letters")
	except:
		pass

	try:
		if(not (nr_dict["nr_numbers"])):
			nr_dict.pop("nr_numbers")
			# print("removed numbers")
	except:
		pass

	try:
		if(not (nr_dict["nr_symbols"])):
			nr_dict.pop("nr_symbols")
			# print("removed symbols")
	except:
		pass

	if(len(nr_dict)):
		random_index = randint(0,len(nr_dict)-1)
		current_key = list(nr_dict.keys())[random_index]
		
		if(current_key=="nr_letters"):
			nr_dict["nr_letters"]-=1
			password+=choice(letters)

		if(current_key=="nr_numbers"):
			nr_dict["nr_numbers"]-=1
			password+=choice(numbers)

		if(current_key=="nr_symbols"):
			nr_dict["nr_symbols"]-=1
			password+=choice(symbols)

print(password)

#Convert to a list and use shuffle on it 