# Given an array of numbers and a target value, find two numbers that sum equals target. 

numbers = [5,3,6,8,2,4,7]
target = 10
# SOLUTION ONE - Brute Force
# Time Complexity: O(n^2) --> two for loops
# Space Complexity: O(1)
def two_sum_v1(numbers, target):
  for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        print([numbers[i], numbers[j]])

print("Testing Two Sum V1 (Double For Loop)")
print(two_sum_v1(numbers, target)) # [3,7], [6,4], or [8,2]

# SOLUTION TWO - Using Hash Table
# Time Complexity: O(n) - only one for loop
# Space Complexity:  O(n) - storing dict object
def two_sum_v2(numbers, target):
  hash_table = {}
  for i in range(len(numbers)):
    if numbers[i] in hash_table:
      print([hash_table[numbers[i]], numbers[i]])
    else: 
      hash_table[target - numbers[i]] = numbers[i]

print("Testing Two Sum V2 (Hash Table)")
print(two_sum_v2(numbers, target))

 




