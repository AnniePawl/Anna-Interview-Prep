# Given array containing n distinc numbers from 1 to n, find missing number in array. 


def missing_num(arr):
  for num in range(len(arr)+1):
    if num not in arr:
      return num


print(missing_num([0])) # 1
print(missing_num([0,1])) # 2
print(missing_num([3,0,1])) # 2
print(missing_num([9,6,4,2,3,5,7,0,1])) # 8


def missing_num2(arr):
  