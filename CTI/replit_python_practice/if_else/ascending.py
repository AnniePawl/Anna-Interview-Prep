# Given an int, return YES if digits are in ascending order, else NO 

def ascending(num):
  num_list = [x for x in str(num)]
  return "YES" if num_list == sorted(num_list) else "NO"

  

print(ascending(123)) # YES
print(ascending(321)) # NO



# Given 3 integers, print them in ascending order
def ascending_three(a,b,c):
  return " ".join(map(str, sorted([a,b,c])))

print(ascending_three(5,3,7)) # 3 5 7