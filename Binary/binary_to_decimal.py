def binary_to_decimal_shortcut(bin):
  return int(bin, 2)

print('Binary to Decimal Shortcut')
print(binary_to_decimal_shortcut('10')) # 2
print(binary_to_decimal_shortcut('101')) # 5


def binary_to_decimal_brute_force(bin):
  # keep track of decimal amount
  decimal = 0
  # reverse so that index corresponds to power of 2
  reversed_bin_list = [int(x) for x in str(bin)][::-1]
  for i in range(len(reversed_bin_list)):
    if reversed_bin_list[i] == 1:
      decimal += 2**i
  return decimal
 

print('Binary to Decimal Brute Force')
print(binary_to_decimal_brute_force('1010')) # 10
print(binary_to_decimal_brute_force('1000')) # 8