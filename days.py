#!/usr/bin/env python3

# Created by: Austin de Mora
# Created on: May 2021
# This program tells you the number of the day inputted

import math


def main():
    # This function checks what month it is based off a number

    # Input

    chosen_number = input("Enter a number between 1 and 7: ")
    print("")

    # process
    try:
        choose_number_int = int(chosen_number)

        if choose_number_int == 1:
            # Output
            print("It's Sunday!")
        elif choose_number_int == 2:
            # Output
            print("It's Monday!")
        elif choose_number_int == 3:
            # Output
            print("It's Tuesday!")
        elif choose_number_int == 4:
            # Output
            print("It's Wednesday!")
        elif choose_number_int == 5:
            # Output
            print("It's Thursday!")
        elif choose_number_int == 6:
            # Output
            print("It's Friday!")
        elif choose_number_int == 7:
            # Output
            print("It's Saturday!")
        else:
            print("Invalid input")
    except Exception:
        print("This is not a number")


if __name__ == "__main__":
    main()
