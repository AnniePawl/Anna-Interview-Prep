# Return average word len of given string 
# Remove punctuation 

import string

def average_word_len(s):
    lengths = []
    s = s.translate(str.maketrans('','',string.punctuation))
    for word in s.split(" "):
      lengths.append(len(word))
    return sum(lengths)/ len(lengths)

print(average_word_len("Hi all, my name is Tom...I am originally from Australia.")) # 4.2
print(average_word_len("I need to work very hard to learn more about algorithms in Python!")) # 4.08

def average_word_len2(s):
  s = s.translate(str.maketrans('','',string.punctuation))
  lens = []
  for word in s.split(' '):
    lens.append(len(word))
  return sum(lens)/len(lens)


  return s

print(average_word_len2('"Hi all, my name is Tom...I am originally from Australia."'))