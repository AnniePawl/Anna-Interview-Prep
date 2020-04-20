# Given a non-empty string and and integer n, return new string where the char at index n has been removed. Value of n will be a valid index of a char in original string.


def missing_char(str, n):
    return str[:n] + str[n+1:]


print(missing_char('button', 1))  # btton
print(missing_char('kitten', 0))  # itten
print(missing_char('glass', 2))  # glss
