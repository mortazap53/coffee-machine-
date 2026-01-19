# importing:
from core.Menu import MENU
from core.Payment import collecting_money, submitting_price
from core.Engine import checking_resources
from core.Resources import resources, tracking_resources, add_payment, reporting_resources


# functions:
def showing_menu(data):
    for choice in data:
        price = data[choice]["cost"]
        print(f"{choice.title()}" + " ==> " + f"${price}")

def tracking_resource():
    water = MENU[take_order]["water"], milk = MENU[take_order]["milk"], coffee = MENU[take_order]["coffee"]
    return water, milk, coffee




print("<<<  Welcome to the Coffee Machine App  >>>")
reporting_resources()
print(f"Here is the menu:")
showing_menu(MENU)
take_order = input("\nWhat would you like?\n==> ").lower()
checked_resource = checking_resources(take_order, resources)
if checked_resource == "we are at your service":
    collected_money = collecting_money()
    submitted_price = submitting_price(take_order, collected_money)
    print(submitted_price)
    if submitted_price:
        print("We are at your service!")
        if submitted_price == "extra":
            refunded = collected_money - MENU[take_order]["cost"]
            print(f"You paid more than the required amount. Here is the refunded amount of money:{refunded}")
            add_payment(take_order)
            tracking_resources(MENU[take_order]["water"], MENU[take_order]["coffee"], MENU[take_order]["milk"])
    elif not submitted_price:
        print("The payment is not sufficient")






