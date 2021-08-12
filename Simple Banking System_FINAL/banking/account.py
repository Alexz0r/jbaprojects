import random


class BankAcc:
    def __init__(self):
        self.card = self.generate_card_number()
        self.pin = self.generate_card_pin()
        self.balance = 0

    @staticmethod
    def generate_card_number():
        number_str = "400000"
        for _ in range(9):
            number_str += str(random.randint(0, 9))
        number = list(map(int, number_str))
        for i in range(15):
            if i % 2 == 0:
                number[i] *= 2
                if number[i] > 9:
                    number[i] -= 9
        total_sum = sum(number)
        check_sum = (10 - total_sum + int(total_sum / 10) * 10) % 10
        number_str += str(check_sum)
        return number_str

    @staticmethod
    def generate_card_pin():
        number = str(random.randint(0, 9))
        for _ in range(3):
            number += str(random.randint(0, 9))
        return number

    @staticmethod
    def luhn_algo(number_str):
        number = list(map(int, number_str))
        for i in range(16):
            if i % 2 == 0:
                number[i] *= 2
                if number[i] > 9:
                    number[i] -= 9
        total_sum = sum(number)
        if total_sum % 10 == 0:
            return True
        return False
