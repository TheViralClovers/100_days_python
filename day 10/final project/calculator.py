from art import logo
from os import system
print(logo)

def add(num1,num2):
	return num1+num2

def subtract(num1,num2):
	return num1-num2

def multiply(num1,num2):
	return num1*num2

def divide(num1,num2):
	if(num2!=0):
		return num1/num2
	print("can't divide by zero")
	return 0

operations = {
	"+":add,
	"-":subtract,
	"*":multiply,
	"/":divide
}

def calculator(num1,num2,symbol):
	operation_function = operations[symbol]
	return operation_function(num1,num2)

def take_input(num1='empty'):
	if(num1=='empty'):
		num1 = float(input("What's the first number?: "))
		for symbol in operations:
			print(symbol)
		symbol = input("Pick an operation: ")
		num2 = float(input("Enter the second number: "))
		result = calculator(num1,num2,symbol)
		print(f"{num1} {symbol} {num2} = {result}")
	else:
		print("+\n-\n*\n/")
		symbol = input("Pick an operation: ")
		num2 = float(input("Enter the second number: "))
		result = calculator(num1,num2,symbol)
		print(f"{num1} {symbol} {num2} = {result}")
	return result

result = take_input()

while(1):
	user_choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")
	if(user_choice=="y"):
		result = take_input(num1=result)
	else:
		system("cls")
		print(logo)
		result = take_input()