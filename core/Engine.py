from core.Menu import MENU


def checking_resources(order, resources):
    yes = "We are at your service!"
    no = "Sorry, we don't have enough resources for preparing!"
    if resources["water"] >= MENU[order]["water"] and resources["coffee"] >= MENU[order]["coffee"] and resources["milk"] >= MENU["cappuccino"]["milk"]:
        return yes
    else:
        return no
