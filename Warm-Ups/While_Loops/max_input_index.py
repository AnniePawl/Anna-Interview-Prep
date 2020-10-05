# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the index of the first maximum of the sequence.  


def max_input_index():
  a = int(input())
  nums = []
  while a!= 0:
    nums.append(a)
    a = int(input())
  return nums.index(max(nums))


print(max_input_index())