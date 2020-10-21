# Given a num, return the sum of its digits 

def sum_digits(num):
  return sum(int(x) for x in str(num))

print(sum_digits(123)) # 6 

def sum_digits2(num):
  return sum(map(int,str(num)))

print(sum_digits2(345)) # 12
