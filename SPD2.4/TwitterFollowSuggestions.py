# Task: Improve suggestions for accounts to follow. Implement a function that accepts a new user's handle and an array of many other user's handles, which could be very long. Calculate a similartity score between a pair of handles by looking at the letters each contains. Score +1 for each letter in alphabet that occurs in both handles. Score -1 for each lettr that occurs in only onle handle. Your function should return K handles from array that has highest similarly score to new user's handle.
# +1 for each pair of similar letters

# Example execution:
# handles = [‘DogeCoin’, ‘YangGang2020’, ‘HodlForLife’, ‘fakeDonaldDrumpf’, ‘GodIsLove’, ‘BernieOrBust’]
# my_handle = 'iLoveDogs'

handles = ['iLoveDog', 'iHateCat']
my_handle = 'iLoveDogs'
number_of_suggestions = 1


def suggest(new_handle, twitter_handles, k):
  # to access each letter, create an array of letters from each word

  # while the letter im looking for has not been seen, loop thru each letter in handle
  # if I come across same letter, add a point, stop that loop
  # if I do not come across letter, keep looking until end, subtract point

  # letter occurs in my handle, but not in handles

  # Return k most similar handles


    # suggest(‘iLoveDogs’, handles, k=2) should return [‘GodIsLove’, ‘DogeCoin’]

    # Strategies
    # determine score based only on the number of similar letters

    # You could input the original username into a dictionary to keep track of character count - or a set if you dont care about duplicate characters

    # Find the 2 most similar words to this one in the array based on total number of letters in both words minus the number of letters without duplicates

    # You could turn the strings into histograms that count the occurence of chars.
    # Implement only a similarity score helper function, then later use it to find similar handles.
    # Make letter matching case sensitive at first, then later make matching case insensitive.
    #
a = (0, 1, 1, 1, 2, 3, 7, 7, 23)


def count_elements(seq) -> dict:


...     """Tally elements from `seq`."""
...     hist = {}
... for i in seq:
...         hist[i] = hist.get(i, 0) + 1
... return hist

counted = count_elements(a)
counted
