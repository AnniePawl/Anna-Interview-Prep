# You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.


def nth_power(array,n):
  if len(array) > n:
     return array[n]** n
  else:
    return -1

print(nth_power([1,2,3,4], 2)) # 9 b/c 3^2
print(nth_power([1,2,3,4], 6)) # -1