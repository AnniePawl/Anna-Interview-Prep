# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

def sort_by_partiy(array):
  evens = []
  odds = []
  for num in array:
    if num % 2 == 0:
      evens.append(num)
    else:
      odds.append(num)

  return evens + odds

print(sort_by_partiy([1,6,4,3,5,2])) # [6,4,2,1,3,5]


# Using Lambda and Sort 
def sort_by_partiy2(array):
  array.sort(key=lambda x:x%2)
  return array

print(sort_by_partiy2([1,6,4,3,5,2])) # [6,4,2,1,3,5]

# Two Pass 
def sort_by_partiy3(array):
  return ([x for x in array if x % 2 == 0] +
  [x for x in array if x % 2 !=0])

print(sort_by_partiy3([1,6,4,3,5,2])) # [6,4,2,1,3,5]
