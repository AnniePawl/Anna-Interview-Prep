# For a given int, find greatest n where 2 * n is less than or equal to int. Return that exponent value and result 


def power_of_two(x):
  power = 1
  while 2**power <= x:
    power +=1
  return (power-1), 2** (power-1)


print(power_of_two(20)) # 4 16
print(power_of_two(50)) # 5 32