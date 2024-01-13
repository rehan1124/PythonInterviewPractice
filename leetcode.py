# --- Easy ---

# Problem 1: Given an array of integers, return indices of the two numbers such that they add up to a specific target.

def two_sum(num_list, target):
    seen = {}

    for i, num in enumerate(num_list):
        complement = target - num
        if complement in seen:
            print(f"Index-{i}, {num}")
            print(f"Index-{seen[complement]}, {complement}")
            print("----------------")
        seen[num] = i


# two_sum([0, 2, 4, 6, 8, 10], 10)

# Problem 2: Reverse digits of an integer.

def reverse_digits(num):
    new_digit = ""
    while num:
        temp = num % 10
        new_digit += str(temp)
        num = num // 10

    print(new_digit)


# reverse_digits(1234)

# Problem 3: Determine whether an integer is a palindrome.

def is_palindrome(num):
    print(str(num) == str(num)[::-1])


# is_palindrome(121)

# Problem 4: Find the longest common prefix string amongst an array of strings.

def longest_common_prefix(str_list):
    str_list.sort()
    prefix = ""
    for i in range(len(str_list[0])):
        # print(str_list[0][i], str_list[-1][i])
        if str_list[0][i] == str_list[-1][i]:
            prefix += str_list[0][i]
        else:
            break
    print("List of strings:", str_list)
    print("Longest common prefix:", prefix)


# longest_common_prefix(["mint", "mini", "mineral"])

# Problem 5: Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input
# string is valid.

def balanced_paranthesis(sample_str):
    paranthesis_dict = {"{": "}", "[": "]", "(": ")"}
    stack = []
    for items in sample_str:
        if items in paranthesis_dict:
            stack.append(items)
        else:
            if not stack:
                print(False)
                return
            else:
                stack.pop()

    print(not stack)


# balanced_paranthesis("{[()]}{]{}}")  # Not balanced
# balanced_paranthesis("{[()]}")  # Balanced


# Problem 6: Given a sorted array nums, remove the duplicates in-place such that each element appears only once and
# returns the new length.

def remove_duplicates(list1):
    unique_items = []
    for items in list1:
        if items not in unique_items:
            unique_items.append(items)

    print(unique_items, "-->", len(unique_items))


# remove_duplicates([1, 2, 2, 3, 3, 3, 4, 5])


# Problem 7: Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def needle_haystack(n, h):
    if n not in h:
        print(False)
        return

    print(h.index(n))


# needle_haystack("leet", "leetcode")
# needle_haystack("leet", "lllleetcode")


# Problem 8: Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

def search_index(int_list, target_val):
    if target_val in int_list:
        print(int_list.index(target_val))
        return

    for i in range(len(int_list)):
        if target_val > int_list[i]:
            continue
        else:
            int_list.insert(i, target_val)
            print(int_list)
            return


search_index([1, 3, 5, 7, 9], 7)
search_index([1, 3, 5, 9], 7)
