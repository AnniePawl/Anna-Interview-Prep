# Given a list, remove item at index 4 and add it to index 2 and end of list 

def rearrange(nums):
  index4 = nums[4]
  nums.remove(index4) # can also use .pop()
  nums.insert(2, index4)
  nums.append(index4)
  return nums
  


print(rearrange([3,4,5,6,7,8])) # [3,4,7,5,6,8,7]