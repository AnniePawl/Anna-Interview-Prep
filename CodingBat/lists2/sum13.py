# Return sum of numbers in array, returning 0 if empty, except number 13 and number that immediately follows 13

# Method 1 
def sum13(nums):
    sum = 0 
    i = 0 
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            sum += nums[i]
            i +=1
    return sum

# Method 2
def sum13_v2(nums):
    sum = sum(nums)
    while i < len(nums):
        if nums[i] == 13:
            sum -=13
            sum -= nums[i+1]
    return sum

def sum13_v2(nums):
    while 13 in nums:
        if nums.index(13) < len(nums)-1:
            numd.pop(numd.index(13)+1)
        nums.pop(nums.index(13))
    return sum(nums)

# Method 3
# def sum13_v3(nums):
#     while 13 in nums:
#         if nums.index(13) < len(nums)-1:
#             nums.pop(nums.index(13)+1)
#         nums.pop(nums.index(13))
#     return sum(nums)
    # while 13 in nums:
    #     if nums.index(13) < len(nums)-1:
    #         nums.pop(nums.index(13)+1)
    #     nums.pop(nums.index(13))
    # return sum(nums)

# Method 1 
print(sum13([13, 1, 13, 2, 4])) # 4 
print(sum13([1, 2, 2, 1])) # 6
print(sum13([13,13])) # 0

# Method 2  
print(sum13_v2([13, 1, 13, 2, 4])) # 4 
print(sum13_v2([1, 2, 2, 1])) # 6
print(sum13_v2([13,13])) # 0

# Method 3 
# print(sum13_v3([13, 1, 13, 2, 4])) # 4 
# print(sum13_v3([1, 2, 2, 1])) # 6
# print(sum13_v3([13,13])) # 0