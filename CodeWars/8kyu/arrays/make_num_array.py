# Given an integer, create an array with all number up to the number(inclusive)

def make_num_array(n):
  num_array = []
  for i in range(1,n+1):
    num_array.append(i)
  return num_array

def make_num_array2(n):
  return [i for i in range(1, n+1)]

def make_num_array3(n):
  return list(range(1,n+1))


print(make_num_array(5))
print(make_num_array2(10))
print(make_num_array3(15))
    