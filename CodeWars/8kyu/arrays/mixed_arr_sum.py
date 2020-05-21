# Given array if ints and string nums, return sum of total as if all were ints 

def sum_mix(arr):
  sum = 0 
  for num in arr:
    sum += int(num)
  return sum

def sum_mix2(arr):
  return sum(int(num) for num in arr)

print(sum_mix([1,4,"7", 5])) # 17
print(sum_mix2([1,4,"8", 5])) # 18
