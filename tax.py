
#!/usr/bin/env python3
# Created By: Lia Duggan
# Date: October 1st, 2022
# Calculates Tax is Alberta

import constants


def main():
    # get user input
    subtotal = float(input("What is the Subtotal? : $"))

    # calculate the tax amount and the total with tax
    tax = subtotal * constants.TAX_RATE_ALBERTA / 100
    total = subtotal + tax

    # display the tax amount and the total with tax
    print("")
    print("The subtotal you  entered is ${:.2f}".format(subtotal))
    print("The HST is ${0:.2f} and the total is ${1:.2f}".format(tax, total))


if __name__ == "__main__":
    main()
