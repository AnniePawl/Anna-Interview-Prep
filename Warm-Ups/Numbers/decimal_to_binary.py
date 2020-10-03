# Convert a Decimal to Binary without using built-in methods 

def decimal_to_binary(decimal):
  binary = []
  while decimal > 0:
    if decimal % 2 == 0 :
      binary.append(0)
      decimal = decimal//2
    else:
      binary.append(1)
      decimal = decimal//2
  return int("".join(map(str,binary[::-1])))

print(decimal_to_binary(2)) # 10
print(decimal_to_binary(3)) # 11
print(decimal_to_binary(5)) # 101
print(decimal_to_binary(10)) # 1010


