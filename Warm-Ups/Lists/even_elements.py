# Given list of nums, print all even elements 

def even_elements(nums):
  evens = [num for num in nums if num % 2 ==0]
  return " ".join(map(str,evens))
  

print(even_elements([1,2,2,3,4])) # 2 2 4

