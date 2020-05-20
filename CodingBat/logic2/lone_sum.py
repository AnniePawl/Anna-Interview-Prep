#  Given 3 ints, return their sum - But if 2 values are the same, neither counts towards sum 

def lone_sum(a,b,c):
  if a == b == c:
    return 0 
  if a == b:
    return c 
  if a == c:
    return b 
  if b == c:
    return a 
  return a + b + c

def lone_sum_v2(a,b,c):
  sum = 0 
  sum += a if a not in [b,c] else 0
  sum += b if b not in [a,c] else 0
  sum += c if c not in [a,b] else 0
  return sum
  

print(lone_sum(3,2,2)) # 3s 
print(lone_sum(1,2,3)) # 6 
print(lone_sum(15,4,4)) # 15
print(lone_sum(7,7,7)) # 0


print("lone_sum_v2")
print(lone_sum_v2(3,2,2)) # 3s 
print(lone_sum_v2(1,2,3)) # 6 
print(lone_sum_v2(15,4,4)) # 15
print(lone_sum_v2(7,7,7)) # 0