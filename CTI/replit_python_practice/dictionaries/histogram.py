# Given a string, return count of occurances before it 

def histogram(sentence):
  words = {}
  occurances = []
  for word in sentence.split(" "):
    if word not in words:
      words[word] = 1
      occurances.append(0)
    else:
      occurances.append(words[word])
      words[word] +=1
  return occurances


print(histogram("one two one two three two four three"))
# 0 0 1 1 0 2 0 1