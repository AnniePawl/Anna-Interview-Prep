# Given a phrase, return length of last word of string. If last word doesn't exist, return 0. 


def len_last_word(phrase):
  return len(phrase.split(" ")[-1])

print(len_last_word("Hello World")) #5
print(len_last_word("")) #0 
print(len_last_word("Goonight Moon")) #4