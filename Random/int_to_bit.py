# Given 3 bit int, print left pit, then right. 

def two_bit(num):
  binary = []
  while num > 0:
    if num % 2 == 0:
      binary.append(0)
      num = num //2 
    else: 
      binary.append(1)
      num = num // 2
    
  return  "".join(map(str, binary[::-1]))
  
print(two_bit(2)) # 1 0 
print(two_bit(3)) # 1 1 
