# Import the random module here
from random import randint
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_integer = randint(0,len(names)-1)

print(f"{names[random_integer]} is going to buy the meal today!")
