# Given a string (s) and a set of words(d), find longest word in d that is a subsequence of s. 
# Word w is a subsequence of s if some number of chars, possibly 0, can be deleted from s to form w without reordering remaining chars 

# The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
# The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
# The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.

def longest_dict_word(s,d):
  pass

print(longest_dict_word('abppplee', {'able", "ale", "apple", "bale", "kangaroo"'}))