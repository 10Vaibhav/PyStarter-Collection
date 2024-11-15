from Data import resources
from Data import MENU

shouldGo = True


def check_resources(drink):
    sufficient = True

    for item in drink:
        if drink[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            sufficient = False

    return sufficient


def process_coins(quarters, dimes, nickles, pennies):
    quarters_price = 0.25 * quarters
    dimes_price = 0.10 * dimes
    nickles_price = 0.05 * nickles
    pennies_price = 0.01 * pennies

    total_amount = quarters_price + dimes_price + nickles_price + pennies_price
    return total_amount


def transaction_check(amount, drink):
    check = False
    drink_amount = MENU[drink]["cost"]

    if amount > drink_amount:
        change = round(amount - drink_amount, 2)
        check = True
        print(f"Here is ${change} dollars in change.")
    elif amount == drink_amount:
        check = True
    else:
        print("Sorry that's not enough money. Money refunded")

    return check


def cash_counter(drink):
    print("Please insert coins.")
    quarter = int(input("how many quarters?: "))
    dime = int(input("how many dimes?: "))
    nickle = int(input("how many nickles?: "))
    pennie = int(input("how many pennies?: "))

    total = process_coins(quarter, dime, nickle, pennie)

    return transaction_check(total, user)


Money = 0
while shouldGo:
    # Tod
    user = input("What would you like 😄? (espresso/latte/cappuccino): ")

    if user == "off":
        shouldGo = False

    elif user == "report":
        print(f"Water 🚰 : {resources['water']} ml\nMilk 🥛 : {resources['milk']} ml\nCoffee 🫘 : {resources['coffee']} g "
              f"\nMoney 💸 : ${Money}")

    elif user == "espresso":
        valid = check_resources(MENU[user]["ingredients"])
        if valid:
            isFine = cash_counter(user)
            if isFine:
                Money += MENU[user]["cost"]
                resources["water"] -= MENU[user]["ingredients"]['water']
                resources["coffee"] -= MENU[user]["ingredients"]['coffee']
                print(f"Here is your {user}☕. Enjoy!")
        else:
            shouldGo = False

    elif user == "latte":

        valid = check_resources(MENU[user]["ingredients"])
        if valid:
            isFine = cash_counter(user)
            if isFine:
                Money += MENU[user]["cost"]
                resources["water"] -= MENU[user]["ingredients"]['water']
                resources["coffee"] -= MENU[user]["ingredients"]['coffee']
                resources["milk"] -= MENU[user]["ingredients"]['milk']
                print(f"Here is your {user} ☕. Enjoy!")
        else:
            shouldGo = False

    elif user == "cappuccino":
        valid = check_resources(MENU[user]["ingredients"])
        if valid:
            isFine = cash_counter(user)
            if isFine:
                Money += MENU[user]["cost"]
                resources["water"] -= MENU[user]["ingredients"]['water']
                resources["coffee"] -= MENU[user]["ingredients"]['coffee']
                resources["milk"] -= MENU[user]["ingredients"]['milk']
                print(f"Here is your {user} ☕. Enjoy!")
        else:
            shouldGo = False
