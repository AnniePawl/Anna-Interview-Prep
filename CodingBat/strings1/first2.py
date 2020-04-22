# Given string, return string made of its first two chars. If string shorter than 2, return whatever there is. If string empty, return empty string


def first_two(str):
    if len(str) >= 2:
        return str[:2]
    else:
        return str


print(first_two('Hello'))  # He
print(first_two('bye'))  # by
print(first_two('w'))  # w
print(first_two(''))
