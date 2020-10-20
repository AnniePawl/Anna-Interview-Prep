# Use set, solve in single line
# Given a list of ints, count number of distinct numbers.


def distinct_num2(nums):
  return len(set(nums))

def distinct_num(nums):
  print(sum(1 for x in set(nums)) -1) 

print(distinct_num([1,2,3,2,1])) # 3
print(distinct_num([1,1,1,1,2])) # 2
