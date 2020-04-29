# Return sum of numbers in array, except ignore sections of numbers starting with 6 and extending to next 7. Every 6 will be followed by at least one 7


def sum67(nums):
    count = 0 
    blocked = False

    for n in nums:
        if n == 6:
            blocked = True
            continue 
        if n == 7 and blocked:
            blocked = False 
            continue 
        if not blocked:
            count += n
    return count


print(sum67([1, 2, 2]))  # 5
print(sum67([1, 2, 2, 6, 99, 99, 7]))  # 5
print(sum67([1, 1, 6, 7, 2]))  # 4
