# A car can cover N km per day. How many days will it take to cover M km ? 

import math

def car_route(n, m):
  return math.ceil(m/n) 

print(car_route(700,750)) # 2 