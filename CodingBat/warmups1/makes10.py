# Given 2 integers, a and b, return True if one of them is 10 or is their sum is 10


def makes10(a, b):
    return (a+b == 10 or a == 10 or b == 10)


print(makes10(10, 2))  # True
print(makes10(5, 5))  # True
print(makes10(9, 9))  # False
