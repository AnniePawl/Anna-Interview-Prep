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

## Better ways to solve some simple problems 
**Arithmetic Problem:** Given 2 integers and an arithmetic operator, return result 
**Solution One:**
```python
def arithmetic(a, b, operator):
  if operator == "add":
    return a + b 
  elif operator == "subtract":
    return a - b
  elif operator == "divide":
    return a/b
  else:
    return a * b
```
**Upgraded Solution:**
``` python
def arithmetic_v2(a, b, operator):
  return {
    'add': a + b, 
    'subtract': a - b, 
    'multiply': a * b, 
    'divide': a /b
  } [operator]
```
**Create Phone Number Problem:** Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
**Solution One:**
```python
def create_phone_number(number):
  f = "".join(map(str,number[:3]))
  s = "".join(map(str,number[3:6]))
  t = "".join(map(str, number[6:10])) 

  return "(" + f + ") " + s + "-" + t
```
**Upgraded Solution:**
```python
def create_phone_number_v2(number):
  return  "({}{}{}) {}{}{}-{}{}{}{}".format(*number)
```

**Get Middle Problem:** Return middle character of word. If word length is even, return middle 2 characters 

**Solution One:**
```python
def get_middle(s):
  if len(s) == 2:
    return s
  # if word even
  elif len(s) % 2 == 0:
    return s[(len(s)//2)-1: (len(s)//2) +1]
  else:
    return s[len(s)//2]
```
**Upgraded Solution:**
```python
def get_middle_v2(s):
  rturn s[(len(s)-1)/2: len(s)/2+1]
```

**Is Isogram Problem:** Return True if input string is an isogram (no repeating letters, consecutive or non-consecutive). Ignore letter case and assume empty string is isogram 
**Solution One:**
```python
def is_isogram(string):
  # make everything lowercase 
  lower_string = string.lower()
  # append letters to list 
  letter_list = []
  for letter in lower_string:
    if letter in letter_list:
      return False 
    else: letter_list.append(letter)
  return True
```
**Upgraded Solution:**
```python
def is_isogram_v3(string):
  return len(string) == len(set(string.lower()))
```

**Front 9 Problem:** Given an array on integers, return True if one of first 4 elements in the array is 9. The array might be less than 4.<br>
**Solution One**
```python
def array_front9(nums):
    end = len(nums)
    if end > 4:
        end = 4
    for i in range(end):
        if nums[i] == 9:
            return True
    return False
```
**Upgraded Solution**
```python
def array_front9_v2(nums):
    return nums[:4].count(9) > 0
```
**Front Three Problem:**Given a string of non-negative int n, front = first 3 characters. Return n copies of front<br>
**Solution 1**
```python
def front_times_v3(str, n):
    result = ""
    front = str[:3]
    for i in range(n):
        result += front
    return result
```
**Upgraded Solution:**
```python
def front_times(str,n):
    return str[:3] *n 
```
**String Bits Problem:** Given a string, return new string amde of every other character  starting with first.<br>
**Solution One**
```python
def string_bits_v2(str):
    result = ""
    for i in range(len(str)):
        if i % 2 == 0:
            result += str[i]
    return result
```
**Upgraded Solution:**
```python
def string_bits(str):
    return str[::2]
```
**String Times Problem:** Given a string and a non-negative int n, return a larger string that is n copies of original string
**Solution One:**
```python
def string_times_v2(str, n):
    result = ""
    for i in range(n):
        result += str
    return result
```
**Upgraded Solution:**
```python
def string_times(str, n):
    return str * n
```
**Sum Three:** Given an array of ints length 3, return sum of all elements
**Solution One:**
```python
def sum3(nums):
    result = 0
    for num in nums:
        result += num
    return result
```
**Upgraded Solution:**
```python
def sum3_v2(nums):
    return sum(nums)
```












