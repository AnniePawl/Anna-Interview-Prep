# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of elements of the sequence that are greater than their neighbors above.  

a = int(input())
nums = []
while a != 0:
  nums.append(a)
  a = int(input())

count = 0
for i in range(1, len(nums)): 
  if nums[i] > nums[i-1]:
    count +=1 

print(count)  

# CTI Solution 
prev = next = int(input())
counter = 0 
while next != 0:
  if prev < next:
    counter += 1
  prev,next = next, int(input())

print(counter)
