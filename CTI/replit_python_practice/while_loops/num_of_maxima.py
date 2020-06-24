# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Find how many elements of this sequence are equal to its largest element.

a = int(input())
nums = []
while a != 0:
  nums.append(a)
  a = int(input())
print(nums.count(max(nums)))


# CTI Solution 
maximum = int(input())
counter = 1
a = -1
while a != 0:
  a = int(input())
  if a > maximum:
    maximum, counter = a, 1
  elif a == maximum:
    counter += 1
print(counter)