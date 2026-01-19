from core.Menu import MENU
from main import take_order


def checking_resources(order):
    if resources["water"] >= MENU[order]["water"] and resources["coffee"] >= MENU[order]["coffee"] and resources["milk"] >= MENU["cappuccino"]["milk"]:
        return True
    else:
        return False

checked_resource = checking_resources(take_order)

def reporting_resources():
    print("Here is the report of our supplies, consider it while ordering! Thanks!")
    print(f"water = {resources["water"]}ml\ncoffee = {resources["coffee"]}gr\nmilk = {resources["milk"]}gr\nmoney = ${resources["money"]}\n")

def tracking_resources(water, coffee, milk):
    if checked_resource:
        resources["water"] -= water
        resources["coffee"] -= coffee
        resources["milk"] -= milk
        return resources
    else:
        return ""

def add_payment(ordered):
    resources["money"] += MENU[ordered]["cost"]

resources = {
    "water": 500,
    "coffee": 500,
    "milk": 300,
    "money": 0,
}