# Return YES if 3 digits, else NO

def three_digits(num):
  return "YES" if len(str(num)) == 3 else "NO"

print(three_digits(123)) # YES
print(three_digits(1233)) # NO