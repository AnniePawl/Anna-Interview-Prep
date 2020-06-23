# Given 3 ints, 2 are the same. Print the order number of the different one (1,2,3)

def order_of_outlier(nums):
  for num in nums:
    if nums.count(num) == 1:
      return nums.index(num) + 1

print(order_of_outlier([10,5,10])) # 2 
print(order_of_outlier([10,10,5])) # 3 