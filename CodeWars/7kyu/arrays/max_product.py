# Given an array, find max product by multiplying 2 adjacent numbers in array 


def max_product(arr):
  max_product = arr[0] * arr[1]
  for i in range(len(arr)-1):
    subset = arr[i] * arr[i+1]
    if subset > max_product:
      max_product = subset
  return max_product


  
print(max_product([5,8])) # 40
print(max_product([1,2,3])) # 6
print(max_product([4, 12, 3, 1, 5])) # 48
print(max_product([5, 1, 2, 3, 1, 4])) # 6
print(max_product([-23, 4, -5, 99, -27, 329, -2, 7, -921])) # -14

# One-liner 

def max_product2(arr):
  return max(arr[i]*arr[i+1] for i in range(len(arr)-1))

