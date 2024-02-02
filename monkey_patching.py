"""
Source:
https://www.youtube.com/watch?v=QtoFo9bXi6w
https://www.youtube.com/watch?v=GQGw3nEmv0E

https://www.youtube.com/watch?v=afGe8LYGlWE
https://www.youtube.com/watch?v=fvaoT5P4aMk
"""

"""class M:
    def m1(self):
        return "I am m1 method."


a = M()
print("--- Before monkey patching ---")
print(a.m1())


def m2():
    return "I am m2 method."


a.m1 = m2
print("--- After monkey patching ---")
print(a.m1())"""


class Power:
    def square(self, n):
        return f"I square anything on my way: {n ** 2}"


def cube(n):
    return f"I cube everything that's given to me: {n ** 3}"


print("--- Before monkey patching ---")
p1 = Power()
print(p1.square(2))

print("--- After monkey patching ---")
p1.square = cube
print(p1.square(2))
