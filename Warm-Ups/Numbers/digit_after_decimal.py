# Return the digit after decimal place 

def dig_decimal(num):
  split_num = str(num).split('.')
  return split_num[1][0]


print(dig_decimal(1.6798)) # 6
print(dig_decimal(98.35)) # 3

def dig_dec(num):
  return int(num * 10) % 10

print(dig_dec(4.566)) # 5