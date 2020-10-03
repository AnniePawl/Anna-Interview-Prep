# Given a two digit int, use division operator to obtain tens place, then remainer for obrainting 

def two_digits(num):
  print("10s place")
  print(num // 10) # divide by 10 to access 10s place
  print("1s place")
  print(num % 10) # use modulo to find remainder
  return str(num // 10) + " " + str(num % 10)

print(two_digits(79)) # 7 9