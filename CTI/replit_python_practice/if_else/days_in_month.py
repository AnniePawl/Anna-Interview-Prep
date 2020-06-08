# Given a month (int between 1 and 12), print numbers of days in that month 

# 30 - 9,4,6,11
# 31 all the rest 
# 28 - 2

def days(num):
  if num in [9,4,6,11]:
    return 30 
  elif num == 2 :
    return 28 
  else: 
    return 31
  

print(days(1)) # 31 
print(days(9)) # 30
print(days(2)) # 28