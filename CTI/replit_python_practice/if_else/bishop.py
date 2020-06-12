# Chess bishop moves diagonally in any number of squares. Given two coordinates, print "YES" if bishop can go from square 1 to square 2, else "NO"

def bishop(nums):
  first_pos = nums[:2]
  second_pos = nums[2:]

  if abs(first_pos[0]- second_pos[0]) == abs(first_pos[1]-second_pos[1]):
    return "YES"
  else:
    return "NO"

print(bishop([4,4,5,5]))




# 5,3 --> (6,4), (7,5), (4,2), (1,7)