"""
input: '[[{(())}]]' output: balanced
input: '[[[(]' output: not balanced
input: '{[]{()}}' output: balanced
"""


def is_balanced(input_str):
    dict1 = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for items in input_str:
        if items in dict1:
            stack.append(items)
        else:
            stack.pop()

    if not stack:
        return True
    return False


# print(is_balanced("[[{(())}]]"))
# print(is_balanced("[[[(]"))
# print(is_balanced("{[]{()}}"))

"""
input = [3, 2, 6, 8, 2, 1, 2, 5, 4, 3, 4]
output = {2:3, 6:1, 8:1, 4:2}
"""

input_list = [3, 2, 6, 8, 2, 1, 2, 5, 4, 3, 4]


def format_input(input_list):
    return {items: input_list.count(items) for items in input_list if items % 2 == 0}


print(format_input(input_list))
