# Given string of text and number k, find k most frequent words in string 

def k_most_frequent(s, k):
  word_count = {}
  for word in s.split():
    if word in word_count:
      word_count[word] +=1
    else:
      word_count[word] = 1

  return word_count
print(k_most_frequent("the sun is here the sun is there the sun is everywhere", 2))