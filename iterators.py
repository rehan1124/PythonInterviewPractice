"""
Source:
https://www.youtube.com/watch?v=Dyu08G2l71c

https://www.youtube.com/watch?v=390dkU2TUCE
"""

# nums = [7, 9, 8, 10]
nums = ["a", 9, "b", 10]

it = iter(nums)
print(type(it))

while it:
    try:
        # print(it)
        print(next(it))
    except StopIteration as si:
        # print("Iteration stopped.")
        break
