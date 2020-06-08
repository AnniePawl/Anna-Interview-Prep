# Given an int, write function to determine if it is a power of 3

def power_of_three(num):
  return 1162261467 % num == 0



print(power_of_three(27)) # true 
print(power_of_three(45)) # false
print(power_of_three(9)) # true 