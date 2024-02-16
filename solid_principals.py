"""
SOLID principles using Python

Single responsibility
Open/Closed
Liskov substitution
Interface segregation
Dependency inversion

https://www.youtube.com/watch?v=pTB30aXS77U

https://www.youtube.com/watch?v=ZkknJI3QMss
https://www.youtube.com/watch?v=acmPg6aV-Zs&list=PLyLkn_nipSjNVOpdOG-nETxKfgEpbubMQ
https://www.youtube.com/watch?v=HLFbeC78YlU&list=PL6n9fhu94yhXjG1w2blMXUzyDrZ_eyOme
"""

from functools import reduce
from abc import ABC, abstractmethod


class Order:
    def __init__(self):
        self._items = []
        self._quantities = []
        self._prices = []
        self._status = "Open"

    def add_item(self, name, quantity, price):
        self._items.append(name)
        self._quantities.append(quantity)
        self._prices.append(price)

    def total_price(self):
        tp = reduce(lambda x, y: x + y, self._prices)
        return tp


class PaymentProcessor:

    @abstractmethod
    def pay(self, order_obj):
        pass


class SmsPaymentProcessor(PaymentProcessor):

    @abstractmethod
    def authorize_user(self, code):
        pass


class DebitPaymentProcessor(SmsPaymentProcessor):
    def __init__(self, security_code):
        self._security_code = security_code
        self._verified = False

    def pay(self, order_obj):
        if not self._verified:
            raise Exception("User is not verified.")
        print("Processing debit payment...")
        print(f"Verifying security code: {self._security_code}")
        order_obj._status = "Paid"

    def authorize_user(self, code):
        print(f"Verifying SMS code: {code}")
        self._verified = True


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self._security_code = security_code
        self._verified = False

    def pay(self, order_obj):
        print("Processing credit payment...")
        print(f"Verifying security code: {self._security_code}")
        order_obj._status = "Paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email):
        self._email = email
        self._verified = False

    def pay(self, order_obj):
        print("Processing paypal payment...")
        print(f"Verifying email: {self._email}")
        order_obj._status = "Paid"


order = Order()
order.add_item("Keyboard", 5, 50)
order.add_item("Mouse", 4, 40)
order.add_item("Charger", 3, 100)
print("Total price for order made:", order.total_price())

dpp = DebitPaymentProcessor(111)
dpp.authorize_user(1234)
dpp.pay(order)
print("++++++++++++++++++++++++++++++++++++++++")
cpp = CreditPaymentProcessor(222)
cpp.pay(order)
print("++++++++++++++++++++++++++++++++++++++++")
ppp = PaypalPaymentProcessor("abc@gmail.com")
ppp.pay(order)
