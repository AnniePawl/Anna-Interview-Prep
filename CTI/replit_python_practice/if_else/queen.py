# Can can move any number of square in any direction. Given 4 coordinates, return YES if queen can move from square 1 to square 2 


def queen(nums):
  first_pos = nums[:2]
  second_pos = nums[2:]

  if abs(first_pos[0]- second_pos[0]) == abs(first_pos[1] - second_pos[1]):
    return "YES"
  elif first_pos[0] == second_pos[0] or first_pos[1] == second_pos[1]:
    return "YES"
  return "NO"

print(queen([1,1,2,2])) # YES
print(queen([5,5,2,7])) # NO