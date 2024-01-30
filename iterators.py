"""
Source:
https://www.youtube.com/watch?v=Dyu08G2l71c
"""

# nums = [7, 9, 8, 10]
nums = ["a", 9, "b", 10]

it = iter(nums)

while it:
    try:
        print(next(it))
    except StopIteration as si:
        # print("Iteration stopped.")
        break
