# GGiven 2 ints, return True is either is 6 or if their sum or difference is 6. 

def love6(a,b):
  return (a ==6 or b ==6) or (abs(a-b) ==6) or (a+b ==6)


  
print(love6(6,1)) # True 
print(love6(4,8)) # False
print(love6(1,5)) # True (sum)
print(love6(20,30)) # False
print(love6(36,6)) # True (difference)
