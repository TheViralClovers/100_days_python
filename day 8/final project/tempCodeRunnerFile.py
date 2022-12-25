user_choice = input("Do you want to \n1)Encrypt \n2)Decrypt\n")
if(user_choice==1):
	user_input = input("Enter a message to encrypt: ")
	shift = int(input("Enter the shift value: "))
	encrypt(user_input,shift)

if(user_choice==2):
	user_input = input("Enter a message to decrypt: ")
	shift = int(input("Enter the shift value: "))
	decrypt(user_input,shift)
# user_choice = input("Do you want to continue? ")
# if(user_choice!="yes"):