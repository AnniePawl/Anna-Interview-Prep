# Return negative - if number already negative, just return num. 0 is 0 

def return_neg(n):
  return n * -1 if n > 0 else n

print(return_neg(0)) # 0
print(return_neg(-5)) # -5
print(return_neg(10)) # -10