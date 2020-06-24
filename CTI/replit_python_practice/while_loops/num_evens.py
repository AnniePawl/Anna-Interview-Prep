# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of even elements of the sequence.  

a = int(input())
nums = []
while a != 0:
  if a % 2 == 0:
    nums.append(a)
  a = int(input())
print(len(nums))
