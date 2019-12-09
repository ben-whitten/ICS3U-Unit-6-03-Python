#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: December 2019
# This is a program which generates 10 random numbers and finds the lowest.

import random


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def minimum_number(list_of_numbers):

    lowest_number = list_of_numbers[0]

    for a_single_number_from_list in list_of_numbers:
        if a_single_number_from_list < lowest_number:
            lowest_number = a_single_number_from_list

    return lowest_number


def main():
    # This is what runs the program.

    random_number = []

    string_of_rounds = input("Input how many numbers you'd like to generate: ")
    min_as_string = input("What do you want the minimum number to be: ")
    max_as_string = input("What do you want the maximum number to be: ")

    try:
        number_of_rounds = int(string_of_rounds)
        minimum = int(min_as_string)
        maximum = int(max_as_string)

        for loop_counter in range(0, number_of_rounds):
            number = random.randint(minimum, maximum)
            random_number.append(number)
            print(color.YELLOW + "{0}".format(random_number[loop_counter]),
                  end=" | " + color.END)

        lowest_number = minimum_number(random_number)
        print("")
        print(color.GREEN + "Lowest = {0}".format(lowest_number) + color.END)

    except Exception:
        print('')
        print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
              ' number...' + color.END)
        print("")
        print("")


if __name__ == "__main__":
    main()
