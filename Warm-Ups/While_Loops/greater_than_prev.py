# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of elements of the sequence that are greater than their neighbors above.  

def greater_than_prev():
  prev = next = int(input())
  count = 0 
  while next != 0:
    if prev > next:
      count += 1
    prev, next = next, int(input())
  return count


def greater_than_prev2():
  a = int(input())
  nums = []
  while a !=0:
    nums.append(a)
    a = int(input())
  
  count = 0 
  for i in range(1,len(nums)):
    if nums[i] > nums[i-1]:
      count+=1
  
  return count

print(greater_than_prev2())
# 1
# 2
# 3
# 4
# 5
# 0

# Answer: 4 