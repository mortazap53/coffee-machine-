from core.Menu import MENU


def checking_resources(order, resources):
    yes = "There is sufficient resources for preparing!"
    no = "Sorry, we don't have enough resources for preparing!"
    if resources["water"] >= MENU[order]["water"] and resources["coffee"] >= MENU[order]["coffee"]:
        if order == "latte" or order == "cappuccino":
            if resources["milk"] >= MENU["cappuccino"]["milk"]:
                return yes
        return yes
    else:
        return no
