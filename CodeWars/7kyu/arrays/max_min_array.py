# Given an array, retun new array with max, followed by min, followed by next max, following by next min etc 

def max_min_arr(arr):
  arr.sort(reverse = True)
  left = 0 
  right = len(arr)-1
  new_arr = []
  while left <= right :
    new_arr.append(arr[left])
    new_arr.append(arr[right])
    left +=1
    right -=1

  return new_arr[:-1] if len(arr) != 0 else new_arr


print(max_min_arr([15,11,10,7,12])) #[15,7,12,10,11]

# CodeWars Solutions 
def solve(arr):
    arr = sorted(arr, reverse=True)
    res = []
    while len(arr):
        res.append(arr.pop(0))
        if len(arr):
            res.append(arr.pop())
    return res



def solve(arr):
    return [sorted(arr)[::-1][(-1)**i*i//2] for i in range(len(arr))]
  

