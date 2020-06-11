# Given 2 uppercase letters, return their postion in alpahbet sequence 

def two_letters(letters):
  position = 0
  letter_list = [letter for letter in letters]
  # First letter
  first_letter_position = ord(letter_list[0]) - 64
  position += 26 * first_letter_position
  position += ord(letter_list[1]) -64
  return position

print(two_letters("AB")) # 28
print(two_letters("KE")) # 291


# AA (26 *1) +1