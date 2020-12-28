def reverse_sequence(n):
  nums = []
  for i in range(1,n+1):
    nums.append(i)
  return nums[::-1]

print(reverse_sequence(5)) # [5,4,3,2,1]


def reverse_sequence2(n):
  return list(range(n,0,-1))

print(reverse_sequence2(5))