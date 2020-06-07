# Given an int, return YES if digits are in ascending order, else NO 

def ascending(num):
  num_list = [x for x in str(num)]
  for i, j in enumerate(num_list):
    if j[i] > j[i-1]:
      return "YES"
    else:
      return "NO"
  
  

print(ascending(123)) # YES
print(ascending(321)) # NO
