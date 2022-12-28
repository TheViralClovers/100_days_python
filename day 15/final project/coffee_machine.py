MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(water, milk, coffee):
    if water > resources["water"]:
        return "water"
    if milk > resources["milk"]:
        return "milk"
    if coffee > resources["coffee"]:
        return "coffee"
    return "ok"


def prepare_drink(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee


def drink_affordability_check(quarters, nickels, dimes, pennies, drink_cost):
    money_inserted = quarters * 0.25 + nickels * 0.05 + dimes * 0.1 + pennies * 0.01
    if money_inserted >= drink_cost:
        change = money_inserted - drink_cost
        is_drink_affordable = True
    else:
        change = money_inserted
        is_drink_affordable = False
    return is_drink_affordable, change


def main():
    continue_condition = True
    money = 0
    while continue_condition:
        user_choice = input("What would you like? (espresso/latte/cappuccino): ")
        if user_choice == "off":
            continue_condition = False
        if user_choice == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money}")
        if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            water_cost = MENU[user_choice]["ingredients"].get("water", 0)
            milk_cost = MENU[user_choice]["ingredients"].get("milk", 0)
            coffee_cost = MENU[user_choice]["ingredients"].get("coffee", 0)
            drink_cost = MENU[user_choice]["cost"]
            is_drink_feasible = check_resources(water_cost, milk_cost, coffee_cost)
            if is_drink_feasible == "ok":
                print("Please insert coins")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                is_drink_affordable, change = drink_affordability_check(quarters, dimes, nickels, pennies, drink_cost)
                if is_drink_affordable:
                    prepare_drink(water_cost, milk_cost, coffee_cost)
                    print(f"Here is ${change:.2f} in change")
                    print(f"Here your {user_choice}☕ Enjoy!")
                    money += drink_cost
                else:
                    print(f"Sorry that's not enough money. Money refunded.")
            else:
                print(f"Sorry there is not enough {is_drink_feasible}.")


main()
