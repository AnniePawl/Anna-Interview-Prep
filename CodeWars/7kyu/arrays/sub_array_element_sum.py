# Given array of arrays, return sum of specific set of numbers, starting with elements whose position is equal to main array len and going down by one at a time. 



def elements_sum(arr, d = 0 ):
  return sum(r[i] if i<len(r) else d for i, r in enumerate(reversed(arr)))
    
def elements_sum2(arr, d= 0):
  position = len(arr)
  sum = 0 
  for num in arr:
    if len(num) >= position:
      sum += num[position-1]
    else: 
      sum += d 
    position -= 1
  return sum

print(elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]])) # 16 (1 + 6 + 9)
print(elements_sum([[3, 2], [4], []])) # 0 
print(elements_sum([[3, 2, 1, 0], [4, 6, 5, 3, 2], []])) # 7


print(elements_sum2([[3, 2, 1, 0], [4, 6, 5, 3, 2], [9, 8, 7, 4]])) # 16 (1 + 6 + 9)
print(elements_sum2([[3, 2], [4], []])) # 0 
print(elements_sum2([[3, 2, 1, 0], [4, 6, 5, 3, 2], []])) # 7