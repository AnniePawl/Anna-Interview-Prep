# Given 3 intns, return sum. But if any value is a teen, it doesn't count (unless its 15 or 16). 
# Write helper function fix_teen that takes in int and returns value fiexed for teen rule to avoid repeating code 3 times 


def fix_teen(n):
  if n in [12,13,14,17,18,19]:
    return 0
  return n

def no_teen_sum(a,b,c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)



# print(fix_teen(15)) # 15
# print(fix_teen(16)) # 16
# print(fix_teen(13)) # 0
# print(fix_teen(19)) # 0

print(no_teen_sum(1,2,3)) # 6 
print(no_teen_sum(1,16,1)) # 18 
print(no_teen_sum(2,13,1)) # 3 
print(no_teen_sum(13,15,13)) # 15 