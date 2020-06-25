# Given an array of integers, sort the array into a wave like array and return it, 
# In other words, arrange the elements into a sequence such that a[1] >= a[2] <= a[3] >= a[4] <= a[5] ...

def wave(arr):
  arr.sort()
  for i in range(0, len(arr)-1, 2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
    i = i + 1
  return arr

print(wave([1, 2, 3, 4]))
# [2, 1, 4, 3], or [4, 1, 3, 2]

