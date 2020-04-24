# Given 2 int arrays each length 3, return new array length 2 containing middle elements


def middle_way(a, b):
    return [a[1], b[1]]


print(middle_way([1, 2, 4], [5, 6, 7]))  # [2,6]
print(middle_way([4, 6, 4], [5, 5, 4]))  # [6,5]
print(middle_way([8, 9, 0], [2, 0, 3]))  # [9,0]
