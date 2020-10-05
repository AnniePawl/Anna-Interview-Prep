# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Determine the length of the widest fragment where all the elements are equal to each other.

def widest_fragment(nums):
  max_fragment = 1
  fragment = 1
  for i in range(len(nums)-1):
    if nums[i] == nums[i+1]:
      fragment +=1
      if fragment > max_fragment:
        max_fragment = fragment
    else:
      fragment = 1
  return max_fragment
  

print(widest_fragment([2,2,7,7,7,7,7,7,9,9,9,9,9])) # 6