# Given string of text and number k, find k most frequent words in string 

def k_most_frequent(s, k):
  word_count = {}
  for word in s.split():
    if word in word_count:
      word_count[word] +=1
    else:
      word_count[word] = 1
  
  k_most_frequent = []
  while k > 0:
    most_frequent = (max(word_count, key = word_count.get))
    k_most_frequent.append(most_frequent)
    word_count.pop(most_frequent)
    k -= 1

  return k_most_frequent

print(k_most_frequent("the sun is here the sun is there the sun is everywhere", 3)) # ["the", "sun", "is"]


# Strategy One: Using Counter
# Time Complexity: O(n)
from collections import Counter 
def counter(s):
  words_list = s.split()
  return Counter(words_list).most_common(2)

print(counter("brown dog brown cat brown hen brown dog"))

