def dec_to_binary(a):

  binary = []
  while a > 0:
    if a % 2 == 0:
      binary.append(0)
    else:
      binary.append(1)
    a = a //2 
  return int("".join(map(str,binary[::-1])))
  

print(dec_to_binary(3)) # 11
print(dec_to_binary(5)) # 101
print(dec_to_binary(8)) # 1000