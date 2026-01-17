# importing:
from core.menu import MENU




# functions:
def show_menu(data):
    for choice in data:
        price = data[choice]["cost"]
        print(f"{choice.title()}" + " ==> " + f"${price}")




print("Welcome to the Coffee Machine App")
print("Here is the menu:\n")
show_menu(MENU)
take_order = input("What would you like?")






