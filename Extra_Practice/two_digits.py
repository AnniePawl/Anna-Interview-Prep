# Given 2 digit int, print tens place and ones place using division and remainder operators 

def two_digit(num):
  return " ".join(map(str,[num//10, num %10]))

print(two_digit(79)) # 7 9


def two_digits2(num):
  return str(num//10) + " " + str(num%10)

print(two_digits2(87)) # 8 7