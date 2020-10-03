def bin_to_dec(bin):
  result = 0 
  reversed_bin = [int(x) for x in str(bin)][::-1]
  for i in range(len(reversed_bin)):
    if reversed_bin[i] == 1:
      result += 2 ** i 
  return result

print(bin_to_dec(10)) # 2
print(bin_to_dec(1010)) # 10
print(bin_to_dec(101)) # 5

def bin_to_dec_shortcut(bin):
  return int(bin, 2)


print(bin_to_dec_shortcut('10')) # 2 
print(bin_to_dec_shortcut('1010')) # 10 
