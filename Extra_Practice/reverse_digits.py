# Given an int, print digits in reverse order with space in between 

# Method One
def reverse_digits(num):
  return " ".join([x for x in str(num)][::-1])

print(reverse_digits(1234)) # 4 3 2 1 

# Method 2
def reverse_digits2(num):
  reverse = 0 
  while num > 0: 
    # multiply reverse num by 10, add remainder of num divided by 10 to reverse num
    a = num % 10
    reverse = reverse * 10 + a
    num = num // 10
  return reverse

print(reverse_digits2(9876)) # 6 7 8 9