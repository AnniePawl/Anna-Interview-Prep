# Given array of ints -- every element appears thrice, except one which occurs once 
# Find element that appearce only once 
# Linear Runtime 

# Use bit logic 
# Loop - count number of ones in position and set bit position 
# Linear Time complexity - even tho 2 for loops , first one is constant and doesn't grow w/ size of array 

# For each bit position(32 bits)
# mask = 1 
# count = 1 
  # For each number in array:
    # Count # 1s in that bit position 
    # if x & mask :
      # count +=1 
  # if count %3 !=0:
    #result = result |(bitwise or) mask 
    
  # mask = mask << 1 

def single_num(nums):
  pass 


# Brute Force  bleh 
def single_num_brute_force(nums):
  for num in nums:
    if nums.count(num) == 1:
      return num
      

print(single_num([1,2,3,1,2,3,1,2,3,4])) # 4
print(single_num_brute_force([1,2,3,1,2,3,1,2,3,4])) # 4