# Given array of ints, find min sum which can be obtained from summing each two integers product

def min_sum(arr):
  sum = 0
  sorted_arr = sorted(arr)
  front_i = 0 
  back_i = len(arr)-1
  
  while front_i < back_i:
    sum += sorted_arr[front_i] * sorted_arr[back_i]
    front_i +=1
    back_i -=1
  return sum


def min_sum2(arr):
  arr = sorted(arr)
  return sum(arr[i]* arr[-i-1] for i in range(len(arr)//2))




print(min_sum([5,4,2,3])) # 22 -> 5*2 + 3*4
# [3,2,4,5]
print(min_sum([9,2,8,7,5,4,0,6])) # 74


print(min_sum2([5,4,2,3])) # 22 -> 5*2 + 3*4
# [3,2,4,5]
print(min_sum2([9,2,8,7,5,4,0,6])) # 74