# Reverse given num. Return true if its same as original 

def reverse(num):
  return str(num) == str(num)[::-1]

print(reverse(121)) # True 
print(reverse(221)) # False 


# Practice reversing number as type int 
def reverse_num(num):
  return int(str(num)[::-1])s

print(reverse_num(123))