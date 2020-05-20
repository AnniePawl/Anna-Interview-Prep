# Given number n, return True if in range 1-10 inclusive. But if "outside_mode" is on, return True if number is 1 or less, or 10 or more. 

def in1to10(n, outside_mode):
  return (n in range(1,11) and not outside_mode) or (n<=1 or n>=10) and outside_mode


print(in1to10(5,False)) # True 
print(in1to10(11,False)) # False  
print(in1to10(11,True)) # True 
print(in1to10(-3,False)) # False
print(in1to10(-3,True)) # True
