import string
import random


class Card:
    def __init__(self):
        pass

    def generate_pin(self):
        self.pin = "".join(random.choice(string.digits) for x in range(4))

    def generate_card_number(self):
        account_id = random.randint(1000000000, 9999999999)
        card = str(400000) + str(account_id)
        self.number = card


user_account = Card()


def menu():
    print("1. Create an account")
    print("2. Log into account")
    print("0. Exit")


def menu_2():
    print("1. Balance")
    print("2. Log out")
    print("0. Exit")


def user_input():
    inp = int(input())
    if inp == 1:
        user_account.generate_card_number()
        user_account.generate_pin()
        print("Your card has been created")
        print("Your card number:")
        print(user_account.number)
        print("Your card PIN:")
        print(user_account.pin)
        menu()
        user_input()

    if inp == 2:
        print("Enter your card number:")
        card_number = str(input())
        print("Enter your PIN:")
        pin = input()
        if card_number == user_account.number:
            if pin == user_account.pin:
                print("You have successfully logged in!\n")
                menu_2()
                user_input_2()
            else:
                print("Wrong card number or PIN!")
                menu()
                user_input()
        else:
            print("Wrong card number or PIN!")
            menu()
            user_input()
    if inp == 0:
        print("Bye!")


def user_input_2():
    choice = int(input())
    if choice == 1:
        print("Balance: 0")
        menu_2()
        user_input_2()
    if choice == 2:
        print("You have successfully logged out!")
        menu()
        user_input()
    if choice == 0:
        print("Bye!")


menu()
user_input()
