# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

love_tens_digit=0
love_ones_digit=0
combined_name = name1+name2

love_tens_digit += combined_name.lower().count("t")
love_tens_digit += combined_name.lower().count("r")
love_tens_digit += combined_name.lower().count("u")
love_tens_digit += combined_name.lower().count("e")
love_ones_digit += combined_name.lower().count("l")
love_ones_digit += combined_name.lower().count("o")
love_ones_digit += combined_name.lower().count("v")
love_ones_digit += combined_name.lower().count("e")

love_score = love_tens_digit*10+love_ones_digit

if(love_score<10 or love_score>90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif(love_score>40 and love_score<50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")