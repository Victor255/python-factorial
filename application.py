"Factorial"

import os
import sys

def clear():
    """This cleans the screen"""
    if os.name == ("posix"): 
        os.system("clear")
    elif os.name == ("ce", "nt", "dos"):
        os.system("cls")
clear()

def factorial(number):
    """This creates the factorial of the any number"""
    if number <= 1:
        return 1
    return number * factorial(number-1)

def valid_number():
    """This verifies if the user inserted numbers"""
    clear()
    while True:
        number = raw_input("Insert the number: \n")
        try:
            number = int(number)
            return number
        except ValueError:
            clear()
            print "Insert only numbers please"
    return number

def print_factorial():
    """This ask the number to show the factorial"""
    number = valid_number()
    factorial_number = str(factorial(number))
    clear()
    print "\nThe factorial of %d is %s " % (number, factorial_number)

def other_factorial():
    """This ask is want to see other number"""
    print_factorial()
    while True:
        ask_user = raw_input("\nDo you want to know the factorial of other number?  y/n  ")
        if ask_user == "y":
            print_factorial()
        elif ask_user == "n":
            clear()
            menu()
        else:
            clear()
            print "Only can write -y- or -n-\n"

def menu():
    """This saves the menu"""
    print "Factorial of a number"
    print "Exit"
    while True:
        ask_user = raw_input(" -- ")
        if ask_user == "1" or ask_user == "factorial":
            other_factorial()
        elif ask_user == "2" or ask_user == "exit":
            clear()
            sys.exit()
        else:
            clear()
            print "Invalidate Election\n"
            menu()

if __name__ == '__main__':
    menu()
