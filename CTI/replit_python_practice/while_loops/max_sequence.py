# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the maximum of the sequence.  

a  = int(input())
nums = []
while a != 0:
  nums.append(a)
  a = int(input())
print(max(nums))