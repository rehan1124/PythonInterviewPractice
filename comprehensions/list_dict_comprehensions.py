"""
Source:
https://www.netguru.com/blog/python-list-comprehension-dictionary
https://www.geeksforgeeks.org/python-dictionary-comprehension/
https://blog.ivankahl.com/python-list-and-dictionary-comprehensions/
"""

lc1 = [i ** 2 for i in range(10) if i % 2 == 0]
print("List comprehension:", lc1)

s1 = "TomDickHarry"
dc1 = {char: s1.count(char) for char in s1}
print("Dictionary comprehension:", dc1)
