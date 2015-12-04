"Factorial"

import os
import sys

def clear():
    """THIS CLEANS THE SCREEEN"""
    if os.name == ("posix"):
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")
clear()

def factorial(number):
    """THIS CREATES THE FACTORIAL OF ANY NUMBER"""
    if number <= 1:
        return 1
    return number * factorial(number-1)

def valid_number():
    """THIS VERIFIES IF THE USER INSERTED NUMBERS"""
    clear()
    while True:
        number = raw_input("Insert the number: ")
        try:
            number = int(number)
            return number
        except ValueError:
            print "Insert only numbers please\n"
    return number

def print_factorial():
    """THIS ASK THE NUMBER TO SHOW THE FACTORIAL"""
    number = valid_number()
    factorial_number = str(factorial(number))
    print "\nThe factorial of %d is %s " % (number, factorial_number)

def other_factorial():
    """THIS ASK IS WANT TO SEE OTHER NUMBER"""
    print_factorial()
    while True:
        ask_user = raw_input("\nYou want to enter another number??  y/n  ")
        if ask_user == "y":
            print_factorial()
        elif ask_user == "n":
            clear()
            menu()
        else:
            print "Insert Only y/n Please"

def menu():
    """THIS SHOWS THE MENU"""
    print "(1)Factorial of a number"
    print "(2)Exit"
    while True:
        ask_user = raw_input(" -- ")
        if ask_user == "1" or ask_user == "factorial":
            other_factorial()
        elif ask_user == "2" or ask_user == "exit":
            clear()
            sys.exit()
        else:
            print "\nInvalid Option"

if __name__ == '__main__':
    menu()
