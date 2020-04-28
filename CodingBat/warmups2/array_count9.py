# Given an array of integers, return number of 9s in array


def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count


def array_count9_v2(nums):
    return nums.count(9) 
    # .count() method counts number of occurances 


print(array_count9([9, 1, 1]))  # 1
print(array_count9([9, 3, 9, 2, 9, 1]))  # 3
print(array_count9([9, 9, 9, 9, 9]))  # 5


print(array_count9_v2([1,9,9])) # 2
print(array_count9_v2([9,9,9])) # 3
