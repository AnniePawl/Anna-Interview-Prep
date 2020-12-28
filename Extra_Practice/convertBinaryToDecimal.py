def binaryToDecimal(binary):
  count = 0
  binary = [int(num) for num in str(binary)]
  reversed_binary = binary[::-1]
  for i, value in enumerate(binary):
    if reversed_binary[i] == 0:
      pass 
    else:
      count += 2**i

  return count


print(binaryToDecimal(101)) # 5
print(binaryToDecimal(11)) # 3
print(binaryToDecimal(1010)) # 10py

