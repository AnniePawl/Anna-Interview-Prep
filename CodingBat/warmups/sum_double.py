# Given two integer values, return their sum. But if the two values are the same, return double their sum


def sum_double(a, b):
    if a != b:
        return a+b
    else:
        return a*4


def sum_double2(a, b):
    sum = a+b
    if a == b:
        sum = sum * 2
    return sum


print(sum_double(1, 3))  # 4
print(sum_double(5, 6))  # 11
print(sum_double(3, 3))  # 12
print(sum_double(5, 5))  # 20

print(sum_double2(1, 3))  # 4
print(sum_double2(5, 6))  # 11
print(sum_double2(3, 3))  # 12
print(sum_double2(5, 5))  # 20
