# Return number of even integers in array


def count_evens(nums):
    count = 0
    for num in nums:
        if num % 2 == 0:
            count += 1
    return count

def count_evens_v2(nums):
    count = 0
    for n in nums:
        count-=n%2-1
    return count

print(count_evens([2, 3, 4, 5, 6]))  # 3
print(count_evens([4, 4, 4, 4, 4, 4]))  # 6
print(count_evens([1, 3, 5]))  # 0

print(count_evens_v2([2, 3, 4, 5, 6]))  # 3
print(count_evens_v2([4, 4, 4, 4, 4, 4]))  # 6
print(count_evens_v2([1, 3, 5]))  # 0
