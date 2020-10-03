def dec_to_binary_shortcut(dec):
  return int(format(dec, '08b'))

print('Decimal to Binary Shortcut')
print(dec_to_binary_shortcut(2)) # 10
print(dec_to_binary_shortcut(3)) # 11
print(dec_to_binary_shortcut(5)) # 101
print(dec_to_binary_shortcut(10)) # 1010

def dec_to_binary_brute_force(dec):
  # List to hold 1s and 0s
  binary = []
  # Divide dec by 2 until nothing left 
  while dec > 0:
    # check if there's remainder 
    if dec % 2 == 0:
      binary.append(0)
      # adjust dec to reflect division
      dec = dec //2  # use // b/c want to return whole number
    else: 
      binary.append(1)
      # adjust dec to reflect division
      dec = dec //2
  # remember to reverse binary list
  return "".join(map(str, binary[::-1]))

print("Decimal to Binary Brute Force")
print(dec_to_binary_brute_force(2)) # 10
print(dec_to_binary_brute_force(3)) # 11
print(dec_to_binary_brute_force(5)) # 101
print(dec_to_binary_brute_force(10)) # 1010

def dec_to_binary(dec):
  binary = []
  while dec > 0 :
    if dec % 2 == 0:
      binary.append(0)
      dec = dec /2 
    else:
      binary.append(1)
      dec = dec//2 
  return "".join(map(str, binary[::-1]))

print("Dec to Binary extra practice")
print(dec_to_binary(2)) # 10
print(dec_to_binary(3)) # 11
print(dec_to_binary(5)) # 101
print(dec_to_binary(10)) # 1010