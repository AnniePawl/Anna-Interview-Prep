# Given a real num, print first digit after decimal 

# Method One (using .split())
def dig_after_dec(num):
  return str(num).split(".")[1][0]

print(dig_after_dec(1.56)) # 5
print(dig_after_dec(2.45)) # 4


# Method Two (using math)
def dig_after_dec2(num):
  return int(num * 10) % 10

print(dig_after_dec2(1.67)) # 6
print(dig_after_dec2(124.77)) # 7


# Method Three (using index)
def dig_after_dec3(num):
  num_list = [x for x in str(num)]
  dec_i = (num_list.index("."))
  return num_list[dec_i +1]

print(dig_after_dec3(67.23)) # 2 
print(dig_after_dec3(3445.983)) # 9