# Given 2D array, compute "perimeter sum"
# Perimeter sum defined as sum of all values on outside of array 

def perimeter_sum(a):
  sum = 0 
  for subarray in a[0], a[-1]:
    for num in subarray:
      sum += num 
  if len(a) > 2:
    for subarray in a[1:-1]:
      sum += subarray[0] + subarray[-1]
  return sum 

# one-liner ? 
def perimeter_sum2(a):
  return sum(sum(a[y][i] for i in range(len(a[0])) if any((not y,not i,y==len(a)-1,i==len(a[0])-1))) for y in range(len(a)))

print(perimeter_sum(([1,2,3], [4,5,6],[7,8,9]))) # 40
print(perimeter_sum(([1,2], [3,4]))) # 10 

print(perimeter_sum2(([1,2,3], [4,5,6],[7,8,9]))) # 40
print(perimeter_sum2(([1,2], [3,4]))) # 10 

# [1,2,3]
# [4,5,6]
# [7,8,9]

