# Convert a binary number back to decimal 

def bin_to_decimal(bin):
  decimal = 0
  bin_list = [int(x) for x in bin][::-1]
  for i in range(len(bin_list)):
    if bin_list[i] == 1:
      decimal += 2**i
  return decimal

print(bin_to_decimal('101')) # 5
print(bin_to_decimal('11')) # 3
print(bin_to_decimal('1010')) # 10


