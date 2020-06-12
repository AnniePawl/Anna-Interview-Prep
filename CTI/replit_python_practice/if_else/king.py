# King can move 1 square in any direction. Given 2 coordiantes, return YES if can can get to second square, else NO 

def king(nums):
  first_post = nums[:2]
  second_post = nums[2:]
  if abs(first_post[0]-second_post[0]) < 2 and abs(first_post[1]- second_post[1]) <2:
    return "YES"
  return "NO"
  

print(king([4,4,5,5])) # YES


# 5,4 --> (5,3), (5,5), (6,4), (6,3,), (4,5), (4,3), (5,3), (5,5)