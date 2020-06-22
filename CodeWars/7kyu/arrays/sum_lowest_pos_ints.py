# Return sum of lowest positive nums in array

# O(n log n)
def sum_smallest_nums(arr):
  smallest_num = min(arr)
  arr.remove(smallest_num)
  return smallest_num + min(arr)

# O(n log n)
def sum_smallest2(nums):
  return sum(sorted(nums)[:2])

print(sum_smallest_nums([5, 8, 12, 18, 22])) # 13
print(sum_smallest_nums([25, 42, 12, 18, 22])) # 30

print(sum_smallest2([5, 8, 12, 18, 22])) # 13
print(sum_smallest2([25, 42, 12, 18, 22])) # 30