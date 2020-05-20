#  Given two ints, return their sum. But if sum in range 10-19 inclusive, just return 20

def sorta_sum(a,b):
  return a + b if a + b not in range(10,20) else 20

print(sorta_sum(1,3))  # 4 
print(sorta_sum(1,9))  # 20
print(sorta_sum(20,1))  # 21