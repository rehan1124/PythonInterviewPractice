str1 = "RLRRLLRLRL"


def balanced_str(text):
    ls = 0
    rs = 0
    count = 0
    result = []
    str1 = ""

    for items in text:
        if items == "L":
            ls += 1
            str1 += items
        else:
            rs += 1
            str1 += items

        if ls == rs:
            result.append(str1)
            ls = 0
            rs = 0
            str1 = ""
            count += 1

    return count, result


print(balanced_str(str1))
print(balanced_str("RLLLLRRRLR"))
print(balanced_str("LLLLRRRR"))
print(balanced_str("RLRRRLLRLL"))
