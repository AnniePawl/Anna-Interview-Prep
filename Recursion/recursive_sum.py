# Write a recursive function to return sum of nums 1-10 

def recursive_sum(num):
  # base case 
  if num == 0:
    return 0 
  else:
    return recursive_sum(num-1)

print(recursive_sum(10)) # 55