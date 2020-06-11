# Given an uppercase letter, return position of letter in alpahbet. Use ord() function

def letter_position(letter):
  # Uppercase letters position 1 starts at 65

  return ord(letter) - 64

print(letter_position("A")) # 1
print(letter_position("L")) # 12