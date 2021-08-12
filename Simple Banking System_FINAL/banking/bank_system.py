from account import BankAcc


class BankSystem:
    state = 'logout'
    user_choice = ''
    active_acc_id = -1

    @staticmethod
    def account_create():
        acc = BankAcc()
        print("Your card has been created")
        print("Your card number:")
        print(acc.card)
        print("Your card PIN:")
        print(acc.pin)
        return acc

    def account_login(self, index):
        self.state = 'login'
        self.active_acc_id = index
        print("You have successfully logged in!")

    def choice(self):
        if self.state == 'login':
            self.user_choice = input(Prompts.login)
        if self.state == 'logout':
            self.user_choice = input(Prompts.logout)


class Prompts:
    logout = """
1. Create an account
2. Log into account
0. Exit
"""
    login = """
1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit
"""
