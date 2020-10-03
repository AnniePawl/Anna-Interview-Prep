# Given a two digit int, swap the digits 

def swap_digits(num):
  # only strings can be reversed using[::-1]
  return str(num)[::-1]
  
print(swap_digits(79)) # 97


def swap_digits2(num):
  return str(num%10) + " " + str(num//10)

print(swap_digits2(85)) # 58