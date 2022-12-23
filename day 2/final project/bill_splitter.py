print("Welcome to the tip calculator.")

total_bill = float(input("Enter the total bill: $"))
no_of_people = int(input("Enter the no. of people to split the bill: "))
tip_percent = int(input("What percentage of tip would you like to give? 10,12 or 15? "))

induvidual_cost = (total_bill*(1+(tip_percent/100)))/no_of_people
print(f"Each person should pay ${induvidual_cost:.2f}")
