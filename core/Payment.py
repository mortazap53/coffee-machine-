from core.Menu import MENU


def collecting_money():
    print("pay the price, please!:")
    pennies = float(input("How many pennies?"))
    nickles = float(input("How many nickles?"))
    dimes = float(input("How many dimes?"))
    quarters = float(input("How many quarters?"))
    collected_price = round((0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies), 2)
    print(f"You payed {collected_price}")
    return collected_price

def submitting_price(order, collected_money):
    if MENU[order]["cost"] <= collected_money:
        if MENU[order]["cost"] < collected_money:
            refunded = collected_money - MENU[order]["cost"]
            return f"You paid more than the required amount. Here is the refunded amount of money:{refunded}"
        return "The price is accepted!"
    else:
        return "The price is insufficient.!"