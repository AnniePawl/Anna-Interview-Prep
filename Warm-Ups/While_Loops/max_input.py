def max_input():
  nums = []
  a = int(input())
  while a !=0:
    nums.append(a)
    a = int(input())
  return max(nums)

print(max_input())