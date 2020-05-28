#  Given array of ints, count all pairs and return count

# Works for test cases, but not complete 
def duplicates(arr):
  pairs = 0 
  for num in arr:
    if arr.count(num) > 1:
      pairs +=1
  return pairs //2

# Works for test cases, but not complete 
def duplicates2(arr):
  return sum(1 for num in arr if arr.count(num)>1) //2


# Use set to cover test case with many more values
def duplicates3(arr):
  return sum(arr.count(i)//2 for i in set(arr))
  



print(duplicates([1,2,5,6,5,2])) # 2 
print(duplicates([100,100])) # 1
print(duplicates([0,0,0,0,0,0,0])) # 3
print(duplicates([])) # 0

print(duplicates2([1,2,5,6,5,2])) # 2 
print(duplicates2([100,100])) # 1
print(duplicates2([0,0,0,0,0,0,0])) # 3
print(duplicates2([])) # 0
print(duplicates2([650])) # 0

print("Testing Duplicates 3")
print(duplicates3([1,2,5,6,5,2])) # 2 
print(duplicates3([100,100])) # 1
print(duplicates3([0,0,0,0,0,0,0])) # 3
print(duplicates3([])) # 0
print(duplicates3([650])) # 0
