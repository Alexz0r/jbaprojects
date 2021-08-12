import account
import bank_system
import bank_db


bank = bank_system.BankSystem()
db = bank_db.BankDB()

bank.choice()

while bank.user_choice != "0":

    # Account create
    if bank.state == 'logout' and bank.user_choice == "1":
        db.insert_card(bank.account_create())
        bank.user_choice = ''

    # Login
    if bank.state == 'logout' and bank.user_choice == "2":
        card = input("Enter your card number:")
        pin = input("Enter your PIN:")
        acc_id = db.check_acc(card, pin)
        if acc_id != -1:
            bank.account_login(acc_id)
        else:
            print("Wrong card number or PIN!")
        bank.user_choice = ''

    # Balance check
    if bank.state == 'login' and bank.user_choice == "1":
        balance = db.check_balance(bank.active_acc_id)
        print("Balance: ", balance)
        bank.user_choice = ''

    # Income
    if bank.state == 'login' and bank.user_choice == "2":
        income = int(input("Enter income:"))
        db.add_income(bank.active_acc_id, income)
        print("Income was added!")
        bank.user_choice = ''

    # Transfer
    if bank.state == 'login' and bank.user_choice == "3":
        receiver_id = ''
        money = 0
        is_error = 0
        receiver = input("Enter card number:")

        if account.BankAcc.luhn_algo(receiver) == 0:
            print("Probably you made a mistake in the card number. Please try again!")
            is_error = 1

        if is_error == 0:
            receiver_id = db.check_card(receiver)
            if receiver_id == -1:
                print("Such a card does not exist.")
                is_error = 1

        if is_error == 0:
            money = int(input("Enter how much money you want to transfer:"))
            balance = db.check_balance(bank.active_acc_id)
            if money > int(balance):
                print("Not enough money!")
                is_error = 1

        if is_error == 0:
            db.add_income(bank.active_acc_id, -money)
            db.add_income(receiver_id, money)
            print("Success!")

        bank.user_choice = ''

    # Close account
    if bank.state == 'login' and bank.user_choice == "4":
        db.delete_acc(bank.active_acc_id)
        bank.active_acc_id = -1
        bank.user_choice = ''

    # Log out
    if bank.state == 'login' and bank.user_choice == "5":
        bank.active_acc_index = -1
        bank.state = 'logout'
        print("You have successfully logged out!")
        bank.user_choice = ''

    bank.choice()

print("Bye!")
