# Given odd length array in which all are the same except 1, return single different number 

def stray(arr):
  for num in arr:
    if arr.count(num) == 1:
      return num


print(stray([1,1,1,2,1])) # 2 
print(stray([23,23,54,23,23])) # 54 


def stray_v2(arr):
  return min(arr,key = arr.count)

print(stray_v2([1,2,1,1,1])) # 2
print(stray_v2([20,20,11,20,20])) # 11
