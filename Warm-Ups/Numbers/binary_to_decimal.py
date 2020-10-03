# Convert binary value into decimal without using built-in python methods 

def binary_to_decimal(bin):
  result = 0 
  reversed_bin = [int(x) for x in bin][::-1]
  for i in range(len(reversed_bin)):
    if reversed_bin[i] == 1:
      result += 2**i
  return result

print(binary_to_decimal('1010')) # 10
print(binary_to_decimal('11')) # 3
print(binary_to_decimal('1000')) # 8