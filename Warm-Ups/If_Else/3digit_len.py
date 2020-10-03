# Given a number, return YES if it's 3 digits 


def three_digits(num):
  if len(str(num)) == 3:
    return "YES"
  else:
    return "NO"

print(three_digits(123)) # YES
print(three_digits(87)) # NO