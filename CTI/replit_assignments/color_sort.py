# Create an algorithm that will sort an array of n elements (either red, white, or blue). 
# Integers 0,1,2 represent red, white, blue 
# Perform sorting in place, use constant time - Can't use sorted b/c creates a new list 
# Should be done in O(n) time! Linear time 


def color_sort(colors):
  for i in range(len(colors)):
    if colors[i] == 0:
      colors.insert(0, colors.pop(i))
    if colors[i] == 2:
      colors.append(colors.pop(i)) # append element and delete 
  return colors

print(color_sort([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(color_sort([1,2,2,0,0,1])) # [0,0,1,1,2,2]


def color_sort2(nums):
  left, right = 0, len(nums)-1
  i = 0 
  while i <=right:
    if nums[i] == 0:
      nums[left], nums[i] = nums[i], nums[left]
      left += 1
      i +=1
    elif nums[i] == 2:
      nums[right], nums[i] = nums[i], nums[right]
      right -=1
    else:
       i +=1
    return nums


print(color_sort2([2,0,2,1,1,0])) # [0,0,1,1,2,2]
print(color_sort2([1,2,2,0,0,1])) # [0,0,1,1,2,2]



