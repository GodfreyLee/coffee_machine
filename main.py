import resources

#Store resources
store_resources_water = resources.resources["water"]
store_resources_milk = resources.resources["milk"]
store_resources_coffee = resources.resources["coffee"]
store_account = 0

#User Choice
def user_choice_function():
    user_choice = input("What would you like? espresso/latte/cappuccino)")
    return user_choice

#report function
def report():
    print(f"Water: {store_resources_water} \nMilk: {store_resources_milk} \nCoffee:{store_resources_coffee} \nMoney: ${store_account}")


#Check resources function
def check_resources():
    if required_resources_water > store_resources_water and required_resources_milk > store_resources_milk and required_resources_coffee > store_resources_coffee:
        return False
    else:
        return True

#Process Coins
def process_coins():
    print("Please insert coins")
    number_of_quarters = int(input("How many quarters? "))
    number_of_dimes = int(input("How many dimes? "))
    number_of_nickels = int(input("How many nickles? "))
    number_of_penny = int(input("How many pennies? "))

    total_value = float(number_of_quarters * 0.25 + number_of_dimes * 0.1 + number_of_nickels * 0.05 + number_of_penny * 0.01)

    return format(total_value, ".2f")



#Process Transaction
def process_transaction(sum_user_coins):
    if sum_user_coins > cost:
        change = sum_user_coins - cost
        print(f"Here is ${change} dollars in change.")
        return cost
    if sum_user_coins == cost:
        return cost
    else:
        print("Sorry, you don't have enough. Money refunded")


#Make coffee
def make_coffee():
    global store_resources_coffee
    global store_resources_water
    global store_resources_milk
    store_resources_coffee -= required_resources_coffee
    store_resources_water -= required_resources_water
    store_resources_milk -= required_resources_milk
    print(f"Here is your {user_choice}. Enjoy!")

#Sub Process
def sub_process():
    global store_account
    if required_resources_water > store_resources_water:
        print("Sorry, there is not enough water")
    elif required_resources_milk > store_resources_milk :
        print("Sorry, there is not enough milk")
    elif required_resources_coffee > store_resources_coffee:
        print("Sorry, there is not enough coffee")
    else:
        sum_user_coins = float(process_coins())
        store_account += process_transaction(sum_user_coins)
        make_coffee()

#Main Process
is_true = True
while is_true == True:
    user_choice = user_choice_function()
    if user_choice == "off":
        is_true = False
    elif user_choice == "report":
        report()
    elif user_choice == "latte" or user_choice == "cappuccino":
        selected_choice = resources.MENU[user_choice]
        selected_choice_ingredient = selected_choice["ingredients"]
        required_resources_water = selected_choice_ingredient["water"]
        required_resources_milk = selected_choice_ingredient["milk"]
        required_resources_coffee = selected_choice_ingredient["coffee"]
        cost = selected_choice["cost"]
        sub_process()
    else:
        selected_choice = resources.MENU[user_choice]
        selected_choice_ingredient = selected_choice["ingredients"]
        required_resources_water = selected_choice_ingredient["water"]
        required_resources_milk = 0
        required_resources_coffee = selected_choice_ingredient["coffee"]
        cost = selected_choice["cost"]
        sub_process()