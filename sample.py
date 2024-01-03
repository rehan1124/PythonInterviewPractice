# 1- Reverse integer

sample_init = 12345


def reverse_int(n):
    reversed_int = ""
    while n:
        r = n % 10
        reversed_int += str(r)
        n = n // 10

    return int(reversed_int)


# ri = reverse_int(sample_init)
# print(ri)

# 2- Reverse string

str1 = "Hello, How are you?"


def reverse_str(s):
    # return s[::-1]
    reversed_str = ""
    for i in range(len(s) - 1, -1, -1):
        # print(s[i])
        reversed_str += s[i]

    return reversed_str


# print(reverse_str(str1))

# 3- Number swapping

def swap_numbers(a, b):
    a, b = b, a
    return a, b


# print(swap_numbers(111, 22))


# 4- Reverse a list

def reverse_list(l):
    new_list = []
    for i in range(len(l) - 1, -1, -1):
        new_list.append(l[i])
    return new_list
    # return l[::-1]


# print(f"Reversing list:", reverse_list([1, 3, 5, 7, 9]))

# 5- Get additional elements between 2 lists

def get_additional_elements(l1, l2):
    # list_length = l1 > l2
    additional_elements_list = set()
    for i in set(l1):
        if i not in set(l2):
            additional_elements_list.add(i)

    for j in set(l2):
        if j not in set(l1):
            additional_elements_list.add(j)

    return list(additional_elements_list)


print("Additional elements b/w 2 lists:", get_additional_elements([1, 2, 3], [3, 4, 5, 6]))
