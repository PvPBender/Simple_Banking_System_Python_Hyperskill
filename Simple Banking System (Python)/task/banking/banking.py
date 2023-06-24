from textwrap import dedent
from random import randint


class Accounts:
    accounts_list = {}
    credit_cards = {}
    iin = "400000"  # Issuer Identification Number
    checksum = str(randint(0, 9))  # later Luhn algorithm will be used

    def __init__(self, account_num):
        self.account_num = account_num  # customer account number
        self.credit_card = Accounts.iin + str(account_num) + Accounts.checksum
        self.pin = str(randint(1, 9998)).zfill(4)

        Accounts.credit_cards[self.credit_card] = self.pin

        self.balance = 0

    def get_balance(self):
        print(f"\nBalance: {self.balance}")


def main_menu_ask():
    menu = dedent("""
        1. Create an account
        2. Log into account
        0. Exit
    """).rstrip()
    while True:
        print(menu)
        if (user_pick := input()) in ["1", "2"]:
            return int(user_pick)

        elif user_pick == "0":
            print("\nBye!")
            exit()

        else:
            print(f"{user_pick} is not an option.")


def logged_in_ask():
    menu = dedent("""
        1. Balance
        2. Log out
        0. Exit
    """).rstrip()
    while True:
        print(menu)
        if (user_pick := input()) in ["1", "2"]:
            return int(user_pick)

        elif user_pick == "0":
            print("\nBye!")
            exit()

        else:
            print(f"{user_pick} is not an option.")


def logged_in_menu(credit_card):
    account_num = str(credit_card[6:15])
    while True:
        if (user_pick := logged_in_ask()) == 1:
            Accounts.accounts_list[account_num].get_balance()
        elif user_pick == 2:
            break


def main():
    while True:
        if (user_pick := main_menu_ask()) == 1:
            while (account_num := str(randint(0, 10**9 - 1)).zfill(9)) not in Accounts.accounts_list:
                Accounts.accounts_list[account_num] = Accounts(account_num)

            print("\nYour card has been created")
            print(f"Your card number:\n{Accounts.accounts_list[account_num].credit_card}")
            print(f"Your card PIN:\n{Accounts.accounts_list[account_num].pin}")

        elif user_pick == 2:
            credit_card = input("Enter your card number:\n")
            pin = input("Enter your PIN:\n")

            try:
                if Accounts.credit_cards[credit_card] == pin:
                    print("\nYou have successfully logged in!")
                    logged_in_menu(credit_card)
                else:
                    print("\nWrong card number or PIN!")

            except KeyError:
                print("\nWrong card number or PIN!")


if __name__ == "__main__":
    main()
