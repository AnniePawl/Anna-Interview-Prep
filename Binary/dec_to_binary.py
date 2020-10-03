# Given a number, return it's binary value without using built-in methods 

def dec_to_bin(num):
  binary = []
  while num > 0:
    if num % 2 == 0 :
      binary.append(0)
      num = num // 2  
    else:
      binary.append(1)
      num = num//2
  return "".join(map(str,binary[::-1]))

print(dec_to_bin(3)) # 11
print(dec_to_bin(10)) # 1010
print(dec_to_bin(15)) # 1111
