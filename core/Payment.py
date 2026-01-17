def collecting_money():
    print("pay the price, please!:")
    pennies = float(input("How many pennies?"))
    nickles = float(input("How many nickles?"))
    dimes = float(input("How many dimes?"))
    quarters = float(input("How many quarters?"))
    collected_price = round((0.25*quarters) + (0.10*dimes) + (0.05*nickles) + (0.01*pennies), 2)
    return collected_price

