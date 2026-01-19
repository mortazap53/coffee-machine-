def order_again():
    do_you_want_to_continue = input("Would you like to continue? (Y/N): ")
    if do_you_want_to_continue.lower() == "y":
        return True
    else:
        return False