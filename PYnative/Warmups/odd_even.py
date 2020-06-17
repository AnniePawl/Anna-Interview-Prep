# Given 2 lists (a,b), return new list that contains odd nums from first and even nums from second 


def even_odd_list(a,b):
  new_list = []
  for num in a:
    if num % 2 != 0 :
      new_list.append(num)
  for num in b:
    if num % 2 == 0:
      new_list.append(num)
  return new_list

print(even_odd_list([10,15,20,25], [60,65,70])) # [15,25,60,70]


