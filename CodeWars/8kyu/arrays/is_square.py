# Given an array of nums, go thru each and add to new list. If num has square root, add that - otherwise, square number 
# Square root = num ** .5 power

def is_square(nums):
  squares_list = []
  for num in nums: 
    if (num **.5).is_integer():
      squares_list.append(num ** .5)
    else:
      squares_list.append(num ** 2)
  return squares_list
    
def is_square2(nums):
  return [i ** .5 if (i**.5).is_integer() else i**2 for i in nums]
  



print(is_square([4,3,9,7])) # [2,9,3,49]
print(is_square([2,1])) # [4,1]

print(is_square2([4,3,9,7])) # [2,9,3,49]
print(is_square2([2,1])) # [4,1]