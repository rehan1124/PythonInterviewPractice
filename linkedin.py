"""
1) Write code to filter duplicate elements from an array and print as a list. DONE
2) Input- aaaabbbcccppxxx -->> Output- a4b3c3p2x3 DONE
3) Input- ["flower", "flow", "flight"] --> Output - common prefix -- fl DONE
4) Write code to sort the list of strings using Java collection.
5) Find the longest substring from a given string that doesn't contain any duplicate characters.
6) To get rid of multiple spaces from a string.
7) Count the number of words in a string using HashMap.
8) Remove all white spaces from a string without using replace().
9) Remove duplicate characters from a string and print it.
10) Code for method overloading and method overriding.
"""


# 1) Write code to filter duplicate elements from an array and print as a list.

def filter_duplicate_elements(arr1):
    # filtered_list = []
    # filtered_dict = dict()
    #
    # for items in arr1:
    #     if items not in filtered_dict:
    #         filtered_dict[items] = True
    #         filtered_list.append(items)
    #
    # return filtered_list

    return list(set(arr1))


# print(f"Filtered elements:", filter_duplicate_elements([1, 2, 2, 0, 0, 4, 4, "a", "b"]))


# 2) Input- aaaabbbcccppxxx -->> Output- a4b3c3p2x3


def format_input_str(str1):
    char_count_dict = {}

    for items in str1:
        if items not in char_count_dict:
            char_count_dict[items] = str1.count(items)

    formatted_str = ""
    for items in char_count_dict:
        formatted_str += f"{items}{char_count_dict[items]}"

    return formatted_str


# print(f"Formatted string:", format_input_str("aaaabbbcccppxxx"))

# 3) Input- ["flower", "flow", "flight"] --> Output - common prefix -- fl

def find_common_prefix(list1):
    list1.sort(key=(lambda x: len(x)))

    print("Sorted list:", list1)

    smallest_str = len(list1[0])

    common_prefix = ""

    for i in range(smallest_str):
        if list1[0][i] == list1[-1][i]:
            common_prefix += list1[0][i]
        else:
            break

    return common_prefix


# print("Common prefix:", find_common_prefix(["flower", "flow", "flight"]))

# 4) Write code to sort the list of strings using Java collection.

def sort_str_list(sample_list):
    sample_list.sort(key=lambda x: len(x))
    return sample_list


print("Sorted list of strings:", sort_str_list(["flower", "flow", "flight"]))
