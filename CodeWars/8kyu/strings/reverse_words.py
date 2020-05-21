# Reverse the words in a string

def reverse_words(str):
  word_array = str.split()
  # return word_array[::-1]
  # Now array has to be combined into string again 
  reversed_word_array = word_array[::1]
  return " ".join(reversed_word_array)


print(reverse_words("Hello World")) # World Hello 
print(reverse_words("I am lost")) # lost am I