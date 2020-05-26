# Given array of ints and target value, return len between first adn second occurance of target value (include targets)

def len_between(arr,n):
  distance = []
  if n not in arr:
    return 0 
  else:
    indices = [i for i in range(len(arr)) if arr[i] == n]
    for num in range(indices[0], indices[1]+1):
      distance.append(num)
  return len(distance)


def len_between2(arr,n):
  if arr.count(n) != 2:
    return 0 
  a = arr.index(n)
  b = arr.index(n, a + 1)
  
  return b - a+1
 


print(len_between([1,1], 1)) # 2
print(len_between([1,2,3,1], 1)) # 4
print(len_between([-7, 5, 0, 2, 9, 5], 10)) # 0
print(len_between([-7, 5, 0, 2, 9, 5], 5)) # 5

print(len_between2([1,1], 1)) # 2
print(len_between2([1,2,3,1], 1)) # 4
print(len_between2([-7, 5, 0, 2, 9, 5], 10)) # 0
print(len_between2([-7, 5, 0, 2, 9, 5], 5)) # 5