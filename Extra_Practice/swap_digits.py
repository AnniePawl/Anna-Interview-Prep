# Given a two-digit int, swap it digits and print result 

def swap_digits(num):
  return str(num%10) + " " + str(num//10)

print(swap_digits(48)) # 8 4



def swap_digits2(num):
  return int(str(num)[::-1])

print(swap_digits2(69)) # 9 6 

