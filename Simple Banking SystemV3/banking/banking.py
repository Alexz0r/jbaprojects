import string
import random
import sqlite3


create_str = ('''CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY, number TEXT, 
                pin TEXT, balance INTEGER DEFAULT 0);''')

insert_str = "INSERT INTO card (number, pin) VALUES"


class BankDB:
    def __init__(self):
        self.conn = sqlite3.connect('card.s3db')
        self.cur = self.conn.cursor()
        self.cur.execute("DROP TABLE IF EXISTS card")
        self.cur.execute(create_str)
        self.conn.commit()

    def insert_card(self):
        execute_str = f'{insert_str}({user_account.number}, {user_account.pin});'
        self.cur.execute(execute_str)
        self.conn.commit()


class Card:
    def __init__(self):
        pass

    def generate_pin(self):
        self.pin = "".join(random.choice(string.digits) for x in range(4))

    def generate_card_number(self):
        number_str = "400000"
        for _ in range(9):
            number_str += str(random.randint(0,9))
        number = list(map(int, number_str))
        for index in range(15):
            if index % 2 == 0:
                number[index] *= 2
                if number[index] > 9:
                    number[index] -=9
        total_sum = sum(number)
        check_sum = (10 - total_sum + int(total_sum / 10) * 10) % 10
        number_str += str(check_sum)
        self.number = number_str
        return number_str

    def luhn_algorithm(number_str):
        number = list(map(int, number_str))
        for index in range(16):
            if index % 2 == 0:
                number[index] *= 2
                if number[index] > 9:
                        number[index] -= 9
        total_sum = sum(number)
        if total_sum % 10 == 0:
            return True
        return False


user_account = Card()
db = BankDB()


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
        db.insert_card()
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
