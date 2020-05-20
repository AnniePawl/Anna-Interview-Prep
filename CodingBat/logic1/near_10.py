# Given integer, return True if num within 2 of a multiple of 10. 

def near_10(num):
  # print(num % 10)
  return num%10 <=2 or num%10 >=8

print(near_10(12)) # True 
print(near_10(27)) # False 
print(near_10(48)) # True  