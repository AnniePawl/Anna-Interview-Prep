# For the given integer N calculate the following sum:
# 1³ + 2³ + ... + N³

def sum_cubes(n):
  sum = 0 
  for num in range(1,n+1):
    sum += num**3
  return sum

print(sum_cubes(3)) # 36