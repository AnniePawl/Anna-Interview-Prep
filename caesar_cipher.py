# Shift each letter of the alphabet by a number of letters. If shift takes you past end of alphabet, just rotate back to front of alphabet.

# Hint: Use built-in ord() and chr() functionns
# ord() gives you number representation of a letter (remember uppercase and lowercase letters are represented differently)
# chr()

# Encyption Rule: c = (x + n) % 26

# original_alphabet= abcdefghijklmnopqrstuvwxyz
original_alphabet= 'abc'
# Rotated Alphabet +3: defghijklmnopqrstuvwxyzabc

def caesar_cipher(str, k):
  translation = ''
  for i in range(len(str)):
    char = str[i]

    # Deal w/ uppercase letters
    if char.isupper():
      translation += chr((ord(char) + k-65) % 26 + 65)
      print(ord(char) + k-65 % 26 + 65)
    
      
      
    # Deal w/ lowercase letters
    else:
      translation += chr((ord(char) + k -97) % 26 + 97)

  # print(ord("a"))
  # print(ord("A"))
 
  # return translation
  
  
print(caesar_cipher("A", 2)) #C
# print(caesar_cipher("ABC", 2)) # CDE
# print(caesar_cipher(original_alphabet, 2))
# print(caesar_cipher("hello", 3)) # khoor





# defghijklmnopqrstuvwxyzabc
# print(caesar_cipher('middle-Outz', 2))
# okffng-Qwvb