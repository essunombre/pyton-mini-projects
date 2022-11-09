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
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


# TODO: 1 Prompt User
# TODO: 2 Turn off the machine
def prompt():
    next_order = True
    while next_order:
        user_answer = input(" What would you like? (espresso/latte/cappuccino): ")
        if user_answer == "off":
            next_order = False
            return "Idiota"
        elif user_answer == "report":
            return print_report()
        elif user_answer == "espresso":
            if check_resources(user_answer):
                cash = process_coins()
                print(check_transaction(user_answer, cash, money))

        elif user_answer == "latte":
            if check_resources(user_answer):
                cash = process_coins()
                print(check_transaction(user_answer, cash))

        elif user_answer == "cappuccino":
            if check_resources(user_answer):
                cash = process_coins()
                print(check_transaction(user_answer, cash))
        else:
            return user_answer


# TODO: 3 Print the report of all coffee machine resources
def print_report():
    print(
        f"Water: {water_left}ml\n" \
        f"Milk: {milk_left}ml\n" \
        f"Coffee: {coffee_left}g\n" \
        f"Money: ${money}\n"
        )
    return prompt()


# TODO: 4 Check resources sufficient to make a drink
def check_resources(user_answer):
    if user_answer == "espresso":
        water = (MENU["espresso"]["ingredients"]["water"])
        coffee = (MENU["espresso"]["ingredients"]["coffee"])
        if water > water_left:
            return "Sorry there is not enough water."
        elif coffee > coffee_left:
            return "Sorry there is not enough coffee."
        else:
            return True

    elif user_answer == "latte":
        water = (MENU["latte"]["ingredients"]["water"])
        coffee = (MENU["latte"]["ingredients"]["coffee"])
        milk = (MENU["latte"]["ingredients"]["milk"])
        if water > water_left:
            return "Sorry there is not enough water."
        elif coffee > coffee_left:
            return "Sorry there is not enough coffee."
        elif milk > milk_left:
            return "Sorry there is not enough milk."
        else:
            return True
    elif user_answer == "cappuccino":
        water = (MENU["cappuccino"]["ingredients"]["water"])
        coffee = (MENU["cappuccino"]["ingredients"]["coffee"])
        milk = (MENU["cappuccino"]["ingredients"]["milk"])
        if water > water_left:
            return "Sorry there is not enough water."
        elif coffee > coffee_left:
            return "Sorry there is not enough coffee."
        elif milk > milk_left:
            return "Sorry there is not enough milk."
        else:
            return True


# TODO: 5 Process coins
def process_coins():
    print("Please insert coins: ")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))
    quarters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01
    total_coins = quarters + dimes + nickles + pennies
    return total_coins


# TODO: 6 Check transactions
def check_transaction(user_answer, total_coins, money):
    if user_answer == "espresso":
        if total_coins >= espresso_price:
            total_coins -= espresso_price
            money += espresso_price
            if total_coins > 0:
                total_coins = round(total_coins, 2)
                print(f"here is ${total_coins} dollars in change.")
            return make_a_coffee(user_answer)
        else:
            return "Sorry that is not enough money. Money refunded."

    elif user_answer == "latte":
        if total_coins >= latte_price:
            total_coins -= latte_price
            resources["money"] += latte_price
            if total_coins > 0:
                total_coins = round(total_coins, 2)
                print(f"here is ${total_coins} dollars in change.")
            return make_a_coffee(user_answer)
        else:
            return "Sorry that is not enough money. Money refunded."
    elif user_answer == "cappuccino":
        if total_coins >= cappuccino_price:
            total_coins -= cappuccino_price
            resources["money"] += cappuccino_price
            if total_coins > 0:
                total_coins = round(total_coins, 2)
                print(f"here is ${total_coins} dollars in change.")
            return make_a_coffee(user_answer)
        else:
            return "Sorry that is not enough money. Money refunded."


# TODO: 7 Make Coffee
def make_a_coffee(user_answer):
    if user_answer == "espresso":
        print("haber")
        resources["water"] -= 50
        resources["coffee"] -= 18

    elif user_answer == "latte":
        resources["milk"] -= 150
        resources["water"] -= 200
        resources["coffee"] -= 24

    elif user_answer == "cappuccino":
        resources["milk"] -= 100
        resources["water"] -= 250
        resources["coffee"] -= 24

    return f"Here is your {user_answer}. Enjoy!"


milk_left = resources["milk"]
water_left = resources["water"]
coffee_left = resources["coffee"]


latte_price = MENU["latte"]["cost"]
cappuccino_price = MENU["cappuccino"]["cost"]
espresso_price = MENU["espresso"]["cost"]

#print(MENU["espresso"]["ingredients"])
#print(MENU["espresso"]["ingredients"]["water"])

prompt()
