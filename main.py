# importing:
from core.Menu import MENU
from core.Payment import collecting_money
from core.Engine import checking_resources
from core.Resources import resources




# functions:
def show_menu(data):
    for choice in data:
        price = data[choice]["cost"]
        print(f"{choice.title()}" + " ==> " + f"${price}")




print("Welcome to the Coffee Machine App")
print("Here is the menu:\n")
show_menu(MENU)
take_order = input("What would you like?\n==> ").lower()
print(checking_resources(take_order, resources))
# collecting_money()






