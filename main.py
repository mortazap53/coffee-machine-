# importing:
from ContinueOrdering.Continue import order_again
from core.Menu import MENU
from core.Payment import collecting_money, submitting_price
from core.Resources import checking_resources, tracking_resources, add_payment, reporting_resources
from Servingcoffee.serving_coffee import serving_coffee


# functions:
def showing_menu(data):
    for choice in data:
        price = data[choice]["cost"]
        print(f"{choice.title()}" + " ==> " + f"${price}")

def tracking_resource():
    water = MENU[take_order]["water"], milk = MENU[take_order]["milk"], coffee = MENU[take_order]["coffee"]
    return water, milk, coffee




print("<<<  Welcome to the Coffee Machine App  >>>")
Order_again = False
while not Order_again:
    reporting_resources()
    print(f"Here is the menu:")
    showing_menu(MENU)
    take_order = input("\nWhat would you like?\n==> ").lower()
    checked_resource = checking_resources(take_order)
    if checked_resource:
        print("We are at your service!")
        tracking_resources(MENU[take_order]["water"], MENU[take_order]["coffee"], MENU[take_order]["milk"])
        collected_money = collecting_money()
        submitted_price = submitting_price(take_order, collected_money)
        if submitted_price:
            print("The price is accepted!")
            if submitted_price == "extra":
                refunded = collected_money - MENU[take_order]["cost"]
                print(f"You paid more than the required amount. Here is the refunded amount of money:{round(refunded, 2)}")
            add_payment(take_order)
            serving_coffee(take_order)
        elif not submitted_price:
            print("The payment is not sufficient, your payment has been refunded!")
            Order_again = True
    if not checked_resource:
            print("Sorry, we don't have enough resources for preparing! order somthing else.")
    take_order_again = order_again()
    if take_order_again:
        Order_again = False
    elif not take_order_again:
        Order_again = True






