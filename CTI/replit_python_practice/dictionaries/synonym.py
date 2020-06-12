# Given pairs of words, return a specific word's pair 

def synonym(word_dict, word):
  return word_dict[word]


word_dict = {"Hello":"Hi", "Bye":"Goodbye", "List":"Array"}
word = "Bye"

print(synonym(word_dict, word))


