class MyCustomException(Exception):
    pass


def addition():
    assert 2 + 3 == 6, "I will continue with execution"


def addition2():
    print("Entering addition2")
    assert 2 + 2 == 5


try:
    addition()
except MyCustomException as mce:
    print(mce)
addition2()
