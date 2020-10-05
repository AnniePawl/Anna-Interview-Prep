# Given a sequence of non-negative integers, where each number is written in a separate line. The sequence ends with 0. Print the number of even elements of the sequence.  


def count_even_input():
  nums = []
  a = int(input())
  while a != 0:
    nums.append(a)
    a = int(input())
  return sum(1 for num in nums if num % 2 == 0)
  

print(count_even_input())

