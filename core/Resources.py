from core.Menu import MENU


def reporting_resources():
    print("Here is the report of our supplies, consider it while ordering! Thanks!")
    print(f"water = {resources["water"]}ml\ncoffee = {resources["coffee"]}gr\nmilk = {resources["milk"]}gr\nmoney = ${resources["money"]}\n")

def tracking_resources(water, coffee, milk):
    resources["water"] = resources["water"] - water
    resources["coffee"] = resources["coffee"] - coffee
    resources["milk"] = resources["milk"] - milk
    return resources

def add_payment(ordered):
    resources["money"] += MENU[ordered]["cost"]

resources = {
    "water": 500,
    "coffee": 500,
    "milk": 300,
    "money": 0,

}