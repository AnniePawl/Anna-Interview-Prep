# Knight moves in an L. Given 2 coordinates, return "YES" if knight can move from square 1 to square 2 

def knight(nums):
  pos1 = nums[:2]
  pos2 = nums[2:]

  if abs(pos1[0]- pos2[0]) == 2 and abs(pos1[1]-pos2[1]) ==1 or abs(pos1[0]- pos2[0]) == 1 and abs(pos1[1]-pos2[1]) ==2:
    return "YES"
  return "NO"

print(knight([2,4,3,2])) # YES
print(knight([5,4,2,4])) # NO



# 5,4 --> (6,2),(6,5), (3,3), (3,5),(4,2),(4,6), (7,3), (7,5), 