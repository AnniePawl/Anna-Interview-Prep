# Given a string, return a string where for every char in original, there are two chars


def double_char(str):
    result = ""
    for i in range(len(str)):
        double = str[i] * 2
        result = result + double
        # result = result + (str[i] * 2)
    return result


print(double_char("ABC"))  # AABBCC
print(double_char("The"))  # TThhee
print(double_char("Hippo"))  # HHiippoo
