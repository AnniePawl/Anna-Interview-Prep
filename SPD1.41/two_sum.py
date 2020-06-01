# Given array of numbers and target value, find two nums that sum to target. 


# Brute Force
# Time Complexity: O(n^2) --> two for loops
# Space Complexity: O(1)
def two_sum(arr, target):
  for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
      if arr[i] + arr[j] == target:
        return ([arr[i], arr[j]])
  return "no values sum to target"

print(two_sum([5,3,6,8,2,4,7], 10)) # [3,7] or [6,4] or [8,2]


# Hash Table Solution
# Time Complexity: O(n) - only one for loop
# Space Complexity:  O(n) - storing dict object
def two_sum_hash(arr, target):
  hash_table = {}
  for i in range(len(arr)):
    if arr[i] in hash_table:
      return [hash_table[arr[i]], arr[i]]
    else:
      hash_table[target - arr[i]] = arr[i]

print(two_sum_hash([5,3,6,8,2,4,7], 10)) 



