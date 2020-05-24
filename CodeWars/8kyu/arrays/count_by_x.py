# Take in two arguments, return arrive of first n multiples of x 

def count_by_x(x,n):
  mults = []
  for num in range(1,n+1):
    mults.append(num * x )
  return mults

def count_by_x2(x,n):
  return [num * x for num in range(1,n+1)]


print(count_by_x(1,5)) # [1,2,3,4,5]
print(count_by_x(2,3)) # [2,4,6]
print(count_by_x(4,5)) # [4,8,12,16,20]

print(count_by_x2(1,5)) # [1,2,3,4,5]
print(count_by_x2(2,3)) # [2,4,6]
print(count_by_x2(4,5)) # [4,8,12,16,20]