# Given an 2 digit int, return it with spaces between 

def num_space(num):
  return str(num // 10) + " " +  str(num%10)

print(num_space(79))  # 7 9)