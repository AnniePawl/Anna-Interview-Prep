# Sum all digits of n, then..
# Subtract sum from n, return n 

def subtract_sum(n):
  num_list = list(map(int,str(n)))
  num_sum = sum(num_list)
  return n - num_sum

print(subtract_sum(12)) # 12- (1+2) ->9
print(subtract_sum(301)) # 301- (3+1) -> 297
