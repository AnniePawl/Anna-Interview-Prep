# Given 2 arrays of ints (a, b), return True if they have the same first element or same last element.


def common_end(a, b):
    return (a[0] == b[0] or b[-1] == a[-1])


print(common_end([1, 2, 3], [1, 3, 5]))  # True
print(common_end([7, 2, 6], [1, 3, 6]))  # True
print(common_end([9, 2, 6], [1, 3, 4]))  # False
