# Repeat string n num of times 
# Return error if not string 

def repeat(word, n):
  if not word.isdigit():
    return word * n
  else:
    "Not a string"

print(repeat("hi", 3)) # hihihi
print(repeat("*", 4)) # ****
print(repeat("Gross", 2)) # GrossGross
print(repeat("123", 3)) # Not a string