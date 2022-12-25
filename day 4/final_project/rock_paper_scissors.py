from random import choice

# Rock
rock = ("""
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
paper = ("""
paper
	 _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
scissors = ("""
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

choice_list = [rock,paper,scissors]
computer_choice = choice(choice_list)
user_choice = choice_list[int(input("Do you want to choose \n1.Rock \n2.Paper \n3.Scissors?\n"))-1]

print(f"You chose {user_choice}")
print(f"Computer chose {computer_choice}")

if(user_choice==computer_choice):
	print("Its a Draw!")

else:
	if(user_choice==rock):
		if(computer_choice==paper):
			print("Computer wins")
		else:
			print("You win")
	elif(user_choice==paper):
		if(computer_choice==rock):
			print("You win")
		else:
			print("Computer wins")
	else:
		if(computer_choice==rock):
			print("Computer wins")
		else:
			print("You win!")