# King can move 1 square in any direction. Given 2 coordiantes, return YES if can can get to second square, else NO 

def king(nums):
  first_post = nums[:2]
  second_post = nums[2:]
  

print(king(4,4,5,5)) # YES