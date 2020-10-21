# Given a string with two words, swap them 


def swap_words(str):
  return " ".join(str.split(" ")[::-1] )

print(swap_words("Hello, world!")) # world! Hello, 