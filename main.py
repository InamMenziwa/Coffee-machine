from coffees import resources,MENU

money = 0
more_customers = True

def calculation(quarters, dimes, nickles, pennies):
    global money,milk,water,coffee
    quarters = quarters * 0.25
    dimes = dimes * 0.10
    nickles = nickles * 0.05
    pennies = pennies * 0.01
    sum_of_money = quarters + dimes + nickles + pennies
    cost = MENU[enter]["cost"]
    resources["water"] = resources["water"] - MENU[enter]['ingredients']["water"]
    if enter != "espresso":
        resources["milk"] = resources["milk"] - MENU[enter]['ingredients']["milk"]
    resources["coffee"] = resources["coffee"] - MENU[enter]['ingredients']["coffee"]
    change = sum_of_money - cost
    money += cost
    if sum_of_money > cost:
        print(f"Here is your change: ${round(change, 2)}")
    else:
        print(f"Sorry not enough money, Your ${sum_of_money} has been refunded")

def selection(report):
        water = report["water"]
        milk = report["milk"]
        coffee = report["coffee"]
        print(f"Water: {water}ml")
        print(f"Milk {milk}ml")
        print(f"coffee: {coffee}g")
        print(f"Money: ${money}")

while more_customers:
    enter = input("what would you like? (espresso/latte/cappuccino): ")

    if enter == "report":
        selection(resources)
    elif enter == "espresso":
        if resources["water"] <= 0 or resources["milk"] <= 0 or resources['coffee'] <= 0:
            print('sorry we out of resources, Your money has been refunded')
        else:
            print('Please insert coins.')
            quarters = float(input("How many quarters?: "))
            dimes = float(input('How many dimes?: '))
            nickles = float(input('How many nickles?: '))
            pennies = float(input('How many pennies?: '))
            calculation(quarters = quarters, dimes=dimes, nickles= nickles, pennies=pennies)
    elif enter == "latte":
        if resources["water"] <= 0 or resources["milk"] <= 0 or resources['coffee'] <= 0:
            print('sorry we out of resources, Your money has been refunded')
            break
        else:
            print('Please insert coins.')
            quarters = float(input("How many quarters?: "))
            dimes = float(input('How many dimes?: '))
            nickles = float(input('How many nickles?: '))
            pennies = float(input('How many pennies?: '))
            calculation(quarters = quarters, dimes=dimes, nickles= nickles, pennies=pennies)
    elif enter == "cappuccino":
        if resources["water"] <= 0 or resources["milk"] <= 0 or resources['coffee'] <= 0:
            print('sorry we out of resources, You money has been refunded')
        else:
            print('Please insert coins.')
            quarters = float(input("How many quarters?: "))
            dimes = float(input('How many dimes?: '))
            nickles = float(input('How many nickles?: '))
            pennies = float(input('How many pennies?: '))
            calculation(quarters = quarters, dimes=dimes, nickles= nickles, pennies=pennies)

