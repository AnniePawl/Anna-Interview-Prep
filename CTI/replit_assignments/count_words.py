# Given a long text string, count the number of occurrences of each word. Ignore case. Assume the boundary of a word is whitespace - a " ", or a line break denoted by "\n". Ignore all punctuation, such as . , ~ ? !. Assume hyphens are part of a word - "two-year-old" and "two year old" are one word, and three different words, respectively. 


def count_words(text):
  text_dict = {}
  for word in text.lower().split(' '):
    if word in text_dict:
      text_dict[word] +=1
    else:
      text_dict[word] = 1

  for key, value in text_dict.items():
    print(key + " " + str(value))



print(count_words("I do not like green eggs and ham, I do not like them, Sam-I-Am"))

# i 2
# do 2
# not 2
# like 2
# green 1
# eggs 1
# and 1
# ham 1
# them 1
# sam-i-am 1