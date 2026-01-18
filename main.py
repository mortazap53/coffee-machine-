# importing:
from core.Menu import MENU
from core.Payment import collecting_money, submitting_price
from core.Engine import checking_resources
from core.Resources import resources, tracking_resources


# functions:
def show_menu(data):
    for choice in data:
        price = data[choice]["cost"]
        print(f"{choice.title()}" + " ==> " + f"${price}")

def tracking_resource():
    water = MENU[take_order]["water"], milk = MENU[take_order]["milk"], coffee = MENU[take_order]["coffee"]
    return water, milk, coffee




print("Welcome to the Coffee Machine App")
print("Here is the menu:\n")
show_menu(MENU)
take_order = input("What would you like?\n==> ").lower()
print(checking_resources(take_order, resources))
collected_money = collecting_money()
print(submitting_price(take_order, collected_money))
tracking_resources(MENU[take_order]["water"], MENU[take_order]["milk"], MENU[take_order]["coffee"])





