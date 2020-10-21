# Given a number, return its 10s digit 

def tens_digit(num):
  return num % 100 // 10

print(tens_digit(1234)) # 3 