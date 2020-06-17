# Determine number of distinct elemnts in num list 

def distinct(nums):
  return len(set(nums))

print(distinct([1,2,2,3,3,3])) # 3


def distinct2(nums):
  distinct = []
  count = 0
  for num in nums: 
    if num in distinct:
      count += 1
    distinct.append(num)
  return count

print(distinct2([1,2,2,3,3,3])) #

# CTI Solition 
# num_distinct = 1
# a = [int(s) for s in input().split()]
# for i in range(1, len(a)):
#   if a[i - 1] != a[i]:
#     num_distinct += 1
# print(num_distinct)
