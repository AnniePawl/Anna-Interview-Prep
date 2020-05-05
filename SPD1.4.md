## SPD 1.4 - Refactoring Assignment 
For this assignment, I went through my interview prep repo and identified problems that could use some refactoring. I analyzed the time and space complexity of my solutions and tried to come up with more efficent answers. 

### Two Sum Problem 
Given an array numbers and a target value , find two numbers whose sum equals target.<br>
**Solution One:** Brute Force 
**Time Complexity:** O(n^2) --> two for loops <br>
**Space Complexity:** O(1) 
```python
numbers = [5,3,6,8,2,4,7]
target = 10

def two_sum_v1(numbers, target):
  for i in range(len(numbers)-1): # O(n)
    for j in range(i+1, len(numbers)): # O(n)
      if numbers[i] + numbers[j] == target:
        print([numbers[i], numbers[j]])

print(two_sum_v1(numbers, target)) # [3,7], [6,4], or [8,2]
```

**Upgraded Solution:** Using Hash Table <br>
**Time Complexity:** O(n) - only one for loop <br>
**Space Complexity:**  O(n) - storing dict object
```python
numbers = [5,3,6,8,2,4,7]
target = 10

def two_sum_v2(numbers, target):
  hash_table = {}
  for i in range(len(numbers)): # O(n)
    if numbers[i] in hash_table:
      print([hash_table[numbers[i]], numbers[i]])
    else: 
      hash_table[target - numbers[i]] = numbers[i]

print(two_sum_v2(numbers, target))
```
### K Largest Problem 
Given an array numbers and a count(k). Find the k largest values in the array.<br>
**Solution One:** Using Sorting <br>
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

print(return_k_largest_values(arr, k))
```
**Upgraded Solution:**  <br>
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

print(k_largest_num(arr, k))
```


