# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the index of the first maximum of the sequence.  

a = int(input())
nums = []
while a != 0:
  nums.append(a)
  a = int(input())

print(nums.index(max(nums))+1)

# CTI Solution
maximum = a = int(input())
maximum_index = 1
i = 1
while a != 0:
  a = int(input())
  i += 1
  if a > maximum:
    maximum = a
    maximum_index = i
print(maximum_index)