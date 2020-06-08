# Given list of nums, print elements w/ even indices

def even_index(nums):
  return " ".join(map(str,[nums[i]for i in range(len(nums)) if i % 2 ==0]))
  

print(even_index([5,6,7,8,9])) # 5 7 9

# CTI Solution 
a = [int(s) for s in input().split()]
for i in a[::2]:
  print(i, sep=" ")

