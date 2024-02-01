"""
Source:
https://www.youtube.com/watch?v=yNzxXZfkLUA
https://www.youtube.com/watch?v=r7Dtus7N4pI MUST WATCH
https://www.youtube.com/watch?v=nYDKH9fvlBY
https://www.youtube.com/watch?v=FsAPt_9Bf3U
https://www.youtube.com/watch?v=PTBZ674EsvI
"""
import datetime
import time

"""def dev_decor(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


def div(a, b):
    return a / b


div = dev_decor(div)
print(div(2, 4))"""

"""def f1(func):
    def wrapper(*args, **kwargs):
        print("--- Start ---")
        func()
        print("--- End ---")

    return wrapper


@f1
def f():
    print("Hello")


f()"""

"""def timer(func):
    def wrapper(*args):
        before = time.time()
        func()
        print(f"Function took {time.time() - before} seconds to execute.")

    return wrapper


@timer
def run():
    time.sleep(2)


run()"""


def log(func):
    def wrapper(*args, **kwargs):
        with open("server_logs.txt", "a") as infile:
            infile.write(
                f"\n{datetime.datetime.now()}: Called {func.__name__}() with arguments {" ".join([str(arg) for arg in args])}")
        val = func(*args, **kwargs)
        return val

    return wrapper


@log
def run(a, b, c):
    return a + b + c


run(1, 3, 5)
