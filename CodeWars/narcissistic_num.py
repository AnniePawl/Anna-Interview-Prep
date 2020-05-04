# A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).  Return True if narcissistic

def narcissistic(value):
  # seperate value into array 
  value_array = [int(i) for i in str(value)]
  sum = 0
  for num in value_array:
    sum  = sum + num ** len(value_array)
  if sum == value:
    return True
  else:
    return False

def narcissistic_v2(value):
  value  =  str(value)
  size = len(value)
  sum = 0 
  for i in value:
    sum += int(i) ** size
  return sum == int(value)
    

print(narcissistic(7)) # True 
print(narcissistic(371)) # True 
print(narcissistic(122)) # False 