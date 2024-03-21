"""
https://youtu.be/PJ4t2U15ACo?si=kSh0GxTC6IEMkRT5

https://www.youtube.com/watch?v=PJ4t2U15ACo&list=PLeo1K3hjS3uub3PRhdoCTY8BxMKSW7RjN
"""
from threading import Thread

import time

sample_list = [2, 3, 4, 5, 6]


def calc_square(arr1):
    for numbers in arr1:
        time.sleep(1)
        print(f"Square of {numbers}: {numbers ** 2}\n")


def calc_cube(arr2):
    for numbers in arr2:
        time.sleep(1)
        print(f"Cube of {numbers}: {numbers ** 3}\n")


if __name__ == "__main__":
    t1 = Thread(target=calc_square, args=(sample_list,))
    t2 = Thread(target=calc_cube, args=(sample_list,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
