# Cound logest consecutive zeros in binary string 

def longest_zeros(str):
  temp = 0
  max = 0 
  for num in str:
    if num == '0':
      temp +=1
    else:
      if temp > max:
        max = temp 
      temp = 0 
  return max

print(longest_zeros('10011000101')) # 3