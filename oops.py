"""
Object-oriented programming:
1) Class 2) Objects 3) Abstraction 4) Polymorphism 5) Encapsulation 6) Inheritance

https://www.youtube.com/watch?v=ZDa-Z5JzLYM&list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc&index=1
https://www.youtube.com/watch?v=EPLz5pKl_jU&list=PLI4OVrCFuY56E57FdYzFNSWcEDS-ZKK26
https://www.youtube.com/watch?v=Ej_02ICOIgs
https://www.youtube.com/watch?v=CD6MJ9pEn2k&list=PLWF9TXck7O_zuU2_BVUTrmGMCXYSYzjku
https://www.youtube.com/watch?v=Mf2RdpEiXjU ONGOING
"""


class Atm:
    def __init__(self):
        # print(f"self's address {id(self)}")
        self._pin = ""
        self._balance = 0
        self.menu()

    def _check_pin(self):
        current_pin = int(input("Enter pin for your account:\n"))
        if current_pin == self._pin:
            return True
        else:
            return False

    def create_new_pin(self):
        self._pin = int(input("Enter new pin:\n"))
        print("New pin has been created.")

    def deposit(self):
        if self._check_pin():
            deposit_money = int(input("Enter amount to deposit:\n"))
            self._balance += deposit_money
            print(f"Amount {deposit_money} has been deposited.")
        else:
            print("Incorrect pin entered.")

    def withdraw(self):
        if self._check_pin():
            withdraw_money = int(input("Enter amount to withdraw:\n"))
            if withdraw_money <= self._balance:
                self._balance -= withdraw_money
                print(f"Amount {withdraw_money} has been withdrawn from your account.")
            else:
                print("Account does not have sufficient balance.")
        else:
            print("Incorrect pin entered.")

    def check_balance(self):
        if self._check_pin():
            print(f"Your account balance is {self._balance}")
        else:
            print("Incorrect pin entered.")

    def exit(self):
        return

    def menu(self):
        options = input("""
        ********************************************
        Hello, how would you like to proceed today?
        1. Enter 1 for creating pin
        2. Enter 2 for changing existing pin
        3. Enter 3 to deposit
        4. Enter 4 to withdraw
        5. Enter 5 to check balance
        6. Enter 6 to exit
        ********************************************
        """)

        match int(options):
            case 1:
                self.create_new_pin()
            case 2:
                print("Change pin.")
            case 3:
                self.deposit()
            case 4:
                self.withdraw()
            case 5:
                self.check_balance()
            case 6:
                self.exit()
            case _:
                print("Please provide valid input.")


# a1 = Atm()
# a1.deposit()
# a1.withdraw()
# a1.check_balance()

"""
OOP demo with Fraction class
"""


class Fraction:
    def __init__(self, n, d):
        self._nume = n
        self._deno = d


f1 = Fraction(2, 3)
print(f1)
