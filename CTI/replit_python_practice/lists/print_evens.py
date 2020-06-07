# Given list of numbers, print all even elements using for loop 

def print_evens(nums):
  return [num for num in nums if num % 2 ==0]
# print(print_evens([1,2,2,3,3,3,4])) # [2,2,4]

a = [int(s) for s in input().split()]
print( " ".join(map(str, ([num for num in a if num % 2 == 0 ])) ))
