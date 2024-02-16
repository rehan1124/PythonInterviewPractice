"""
Source:
https://www.youtube.com/watch?v=3XRSULw-HlE
"""


# --- Nested function ---

def pop(lst):
    def get_last_item():
        return lst[-1]

    lst.remove(get_last_item())
    return lst


input_list = [1, 2, 3, 4, 5]
print("Original list:", input_list)
print("First pop:", pop(input_list))
print("Second pop:", pop(input_list))
print("Third pop:", pop(input_list))


# --- Closures ---

def with_args(text):
    def print_text():
        return text

    return print_text


print("--- Closures ---")
wa = with_args("Hello")
print(wa())
