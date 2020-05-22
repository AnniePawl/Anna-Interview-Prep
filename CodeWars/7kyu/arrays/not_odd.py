# Return values that are not odd 

def not_odd(values):
  not_odd = []
  for num in values:
    if num % 2 == 0:
      not_odd.append(num)
  return not_odd

def not_odd2(values):
  return [num for num in values if num % 2 ==0]

print(not_odd([1,3,4,6,7])) # [4,6]
print(not_odd2([1,3,4,6,7])) # [4,6]