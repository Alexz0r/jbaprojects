import random


my_friends = dict()
n = int(input("Enter the number of friend joining (including you):\n\n"))
if n < 1:
    print("No one is joining for the party")
    exit()
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(n):
        name = input("")
        my_friends[name] = 0

total_bill = int(input("Enter the total bill value:\n\n"))

user_input = input('''Do you want to use the "Who is lucky?" feature? Write Yes/No:\n\n''')
if user_input == "Yes":
    lucky_guy = random.choice(list(my_friends.keys()))
    print(f"{lucky_guy} is the lucky one!")

    final_bill = (total_bill // (n-1))
    if final_bill % 2 == 0:
        final_bill = int(final_bill)

    split_list = dict.fromkeys(my_friends, final_bill)
    split_list[lucky_guy] = 0
    print(split_list)
else:
    print("No one is going to be lucky")
    final_bill = round(total_bill / n, 2)
    if final_bill % 2 == 0:
        final_bill = int(final_bill)
    split_list = dict.fromkeys(my_friends, final_bill)
    print(split_list)
