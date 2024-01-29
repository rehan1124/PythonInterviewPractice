"""
Source: https://www.geeksforgeeks.org/python-oops-concepts/
"""


class Person:
    def __init__(self, name, address, mobile_number, age):
        self._name = name
        self._address = address
        self._mobile_number = mobile_number
        self._age = age

    def details(self):
        print(
            f"Hi!!! I am {self._name}, age {self._age} years. I stay in {self._address}. You can contact with me on {self._mobile_number}.")


class Employee(Person):
    def __init__(self, name, address, mobile_number, age, department_name, salary):
        self._department_name = department_name
        self._salary = salary
        super().__init__(name, address, mobile_number, age)

    def details(self):
        print(
            f"Employee '{self._name}' belongs to '{self._department_name}' department. His/Her current salary is '{self._salary}'.")


p1 = Person("Tom", "Bangalore", "1234567890", 35)
p1.details()

e1 = Employee("Harry", "Kochi", "0987654321", 36, "DevQa", 35000)
e1.details()
