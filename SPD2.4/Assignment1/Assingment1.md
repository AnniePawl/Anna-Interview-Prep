# SPD 2.4 Assignment 1: Code 2 Solutions for Each Problem

## Problem 1: Two Sum
Given an array numbers and a target value , find two numbers whose sum equals target.<br>

**SOLUTION ONE:** Brute Force <br>
**Time Complexity:** O(n^2) --> two for loops<br>
**Space Complexity:** O(1) 
```python
numbers = [5,3,6,8,2,4,7]
target = 10

def two_sum_v1(numbers, target):
  for i in range(len(numbers)-1):
    for j in range(i+1, len(numbers)):
      if numbers[i] + numbers[j] == target:
        print([numbers[i], numbers[j]])

print("Testing Two Sum V1 (Double For Loop)")
print(two_sum_v1(numbers, target)) # [3,7], [6,4], or [8,2]
```

**SOLUTION TWO:** Using Hash Table <br>
**Time Complexity:** O(n) - only one for loop <br>
**Space Complexity:**  O(n) - storing dict object
```python
numbers = [5,3,6,8,2,4,7]
target = 10

def two_sum_v2(numbers, target):
  hash_table = {}
  for i in range(len(numbers)):
    if numbers[i] in hash_table:
      print([hash_table[numbers[i]], numbers[i]])
    else: 
      hash_table[target - numbers[i]] = numbers[i]

print("Testing Two Sum V2 (Hash Table)")
print(two_sum_v2(numbers, target))
```
## Problem 2: K Largest Numbers
Given an array numbers and a count(k). Find the k largest values in the array.<br>
**SOLUTION ONE:** Using Sorting <br>
**Time Complexity:** O(nlogn) + O(n) --> b/c sorting and one for loop <br>
**Space Complexity:** 
```python
arr = [4, 3, 27, 30, 9]
k = 2

def return_k_largest_values(arr, k):
    sorted_array = sorted(arr, reverse=True)
    result = []
    for i in range(k):
        result.append(sorted_array[i])
    return result

print("Testing K Largest V1:")
print(return_k_largest_values(arr, k))
```
**SOLUTION Two:**  <br>
**Time Complexity:** O(n)<br>
**Space Complexity:** 
```python 
def simple_largest_num(array):  # overall time o(n)
    largest_num = array[0]  # space O(1)
    for i in range(len(array)):  # time O(n)
        if array[i] > largest_num:  # time O(1)
            largest_num = array[i]  # time O(1)
    return largest_num

def k_largest_num(array, k):  # time 0(k*n)
    result = []  # space O(k)
    while len(result) < k:  # time O(k)
        largest = simple_largest_num(array)  # time o(n)
        array.remove(largest)  # time O(n)
        result.append(largest)  # time O(1)
    return result

print("Testing K Largest V2:")
print(k_largest_num(arr, k))
```

## Problem 3: Complex Two Sum
Given two sorted arrays (a and b) of numbers and a target value, find a number from each array whose sum is closest to target.<br>
**SOLUTION ONE:** <br>
**Time Complexity:** <br>
**Space Complexity:** 
```python
def complex_two_sum(a, b, target):
  possible_solutions = []
  # make left and right pointers
  left= 0
  right= len(b) - 1
  # sort arrays   
  a = sorted(a) 
  b = sorted(b) 

  difference = abs(target - (a[left] + b[right]))
  while (left<= len(a) - 1) and (right>= 0): # O(nm)
      if abs(target - (a[left] + b[right])) < difference:
          
          possible_solutions = [(a[left], b[right])]
          difference = abs(target - (a[left] + b[right]))
      elif abs(target - (a[left] + b[right])) == difference:
          possible_solutions.append((a[left], b[right]))
      if (a[left] + b[right]) < target:
          left+= 1
      elif (a[left] + b[right]) > target:
          right-= 1
      elif (a[left] + b[right]) == target:
          left, right= left+1, right-1
  return possible_solutions

print(complex_two_sum(a,b,target))
```