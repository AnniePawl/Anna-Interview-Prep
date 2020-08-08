a = 15 
b = 27

# '08b'

# This will format at type string
print(format(a,'08b'))
# Convert to integer 
print(int(format(b,'08b')))

# bin(a)
# You can also use bin() - this will return type string w/ 0b infront, indicating value in binary 
print(bin(a))

def dec_to_binary(a):
  return format(a,'08b')

print(dec_to_binary(56))