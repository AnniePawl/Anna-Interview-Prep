# Car can cover N km per day. How many days will it take to cover route of len M km.
import math 

def distance(N,M):
  return math.ceil(M/N)

print(distance(700, 750)) # 2 
print(distance(5, 20)) # 4
print(distance(5, 22)) # 5