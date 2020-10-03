# Given  a number, return YES if digits are in ascending order 

def ascending_order(num):
  num_list =  [int(x) for x in str(num)]
  if num_list == sorted(num_list):
    return "YES"
  else:
    return "NO"

print(ascending_order(179)) # YES
print(ascending_order(893)) # NO