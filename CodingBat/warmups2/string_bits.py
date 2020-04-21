# Given a string, return new string amde of every other character  starting with first.


def string_bits(str):
    return str[::2]


def string_bits_v2(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result


print(string_bits('hello'))  # hlo
print(string_bits('goodbye'))  # gobe


print(string_bits_v2("butterfly"))  # btefy
