# Write recursive function to calculate sum of nums 0-10


def recursive_sum(num):
  # base case 
  if num == 0:
    return num 
  else:
    return num + recursive_sum(num-1)

print(recursive_sum(10))
