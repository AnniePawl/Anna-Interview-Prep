#  Given 4 input nums (1st two = position 1, 2nd two = position 2). Return YES if rook can move from 1st to 2nd square. Else, print no 

def rook(nums):
  first_post = nums[:2]
  second_post = nums[2:]
  if first_post[0] == second_post[0]:
    return "YES"
  elif first_post[1] == second_post[1]:
    return "YES"
  else:
    return "NO"

print(rook([4,4,5,5])) # NO
print(rook([4,4,4,7])) # YES

