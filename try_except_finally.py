class IAmCustomError(Exception):
    pass


try:
    a = 9 / 0
except Exception:
    raise IAmCustomError("I don't divide by ZERO.")
finally:
    print("I will execute always")
