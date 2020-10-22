# Square nums in an array and return total sum 

def square_sum(nums):
  return sum(x**2 for x in nums)
  

print(square_sum([1,2])) # 5 
print(square_sum([0,3,4,5])) # 50 