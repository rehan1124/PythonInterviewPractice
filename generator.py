"""
Source:
https://www.youtube.com/watch?v=mziIj4M_uwk

https://www.youtube.com/watch?v=390dkU2TUCE
https://www.youtube.com/watch?v=lTOtzSDhzi0
"""

"""
# Example-1
def gen_ex():
    yield 1
    yield 2
    yield 3


ge = gen_ex()

print(next(ge))

print("--- Inside for loop now ---")
for items in ge:
    print(items)
"""

"""
# Example-2
def top_ten_square():
    i = 1
    while i <= 10:
        yield i * i
        i += 1


tts = top_ten_square()

for values in tts:
    print(values)
"""
