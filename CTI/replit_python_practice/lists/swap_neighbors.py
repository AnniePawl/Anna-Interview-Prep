# Given a list of numbers, swap adjacent elements in each pair (swap A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element intact.

def swap_neighbors(l):
  for i in range(0,len(l)-1,2):
    l[i], l[i+1] = l[i+1], l[i]
    i = i +1
  return l
 

print(swap_neighbors([1,2,3,4,5])) # [2,1,4,3,5]