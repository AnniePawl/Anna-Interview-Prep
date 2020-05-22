# Determine if sum of numbers is off or even


def odd_or_even(nums):
  sum = 0
  for num in nums:
    sum += num 
  if sum % 2 == 0:
    return ("even")
  else:
    return ("odd")

def odd_or_even2(nums):
  return "even" if sum(nums) % 2 == 0 else "odd"

print(odd_or_even([0,1,4])) # "odd" 
print(odd_or_even([0,-1,-5])) # "even"

print(odd_or_even2([0,1,4])) # "odd" 
print(odd_or_even2([0,-1,-5])) # "even"