# Given 2 lists, create 3rd list with off indexes from list 1 and even indexes from list 2 

def odd_even(list1, list2):
  list3 = []
  for i, j in enumerate(list1):
    if i % 2 != 0:
      list3.append(j)
  for i, j in enumerate(list2):
    if i % 2 == 0:
      list3.append(j)
  return list3


print(odd_even([1,2,3,4,5], [6,7,8,9,10])) # [2,4,6,8,10]