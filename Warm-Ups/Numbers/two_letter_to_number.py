# Given two letters, return their position in the alphabet

def letter_to_num(letters):
  first_position = (ord(letters[0]) - 64) * 26
  second_position = ord(letters[1])-64
  return first_position + second_position

print(letter_to_num('AA')) # 27
print(letter_to_num('KE')) # 291



# To convert a letter to a number, use "ord"
# Subtract 64 to find position in alphabet, since A starts at 65