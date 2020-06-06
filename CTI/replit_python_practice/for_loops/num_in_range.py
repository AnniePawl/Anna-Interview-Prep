# Print inclusive range given 2 nums 
# Return as string w/ space between 

def range_func(a,b):
  nums = []
  for num in range(a, b +1):
    nums.append(num)
  return " ".join(map(str,nums))

def range_func2(a,b):
  for i in range(a, b + 1):
    print(i, end= " ")

def range3(a,b):
  nums = []
  for num in range(min(a,b), max(a,b) + 1):
    nums.append(num)
  return " ".join(map(str,nums[::-1])) if a > b else " ".join(map(str,nums))

print(range_func(4,7)) # 4 5 6 7 
print(range_func2(4,7)) # 4 5 6 7 

print("Range")
print(range3(8,5)) # 8 7 6 5
print(range3(1,4)) # 1 2 3 4

