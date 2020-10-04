# Given two integers, print a thru b inclusively 

def series(a,b):
  nums = []
  for num in range(a,b+1):
    nums.append(num)
  return " ".join(map(str, nums))

print(series(1,6)) # 1 2 3 4 5 6 