# Task: Improve suggestions for accounts to follow. Implement a function that accepts a new user's handle and an array of many other user's handles. Calculate a similartity score between a pair of handles by looking at the letters each contains. Score +1 for each letter in alphabet that occurs in both handles. Score -1 for each lettr that occurs in only onle handle. Your function should return K handles from array that has highest similarly score to new user's handle.

# handles = [‘DogeCoin’, ‘YangGang2020’, ‘HodlForLife’, ‘fakeDonaldDrumpf’, ‘GodIsLove’, ‘BernieOrBust’]
# my_handle = 'iLoveDogs'

# BRAINSTORM
# 1. Use a set?
# 3. Use a histogram ?

from collections import Counter


def my_handle_histogram(my_handle):
    # Create a histogram to keep track letter occurances in my_handle
    my_handle_histogram = {}
    for letter in my_handle:
        if letter in my_handle_histogram:
            my_handle_histogram[letter] += 1
        else:
            my_handle_histogram[letter] = 1
    return my_handle_histogram


# print(my_handle_histogram("iLoveDogs"))


def twitter_handles_histogram(twitter_handles):
    twitter_handles_array = []
    # Use my histogram function to populate ^ array w/ handles histos
    for handle in twitter_handles:
        twitter_handle_histogram = my_handle_histogram(handle)
        twitter_handles_array.append(twitter_handle_histogram)
    return twitter_handles_array


# print(twitter_handles_histogram(
#     ["DogeCoin", "YangGang2020", "HodlForLife", "fakeDonaldDrumpf"]))


def similiary_score(my_handle, twitter_handles):
    # keep track of a score
    scores = {}
    # create a loop to compare letters in my_handle to letters in each twitter_handle
    for i in range(len(twitter_handles)):
        score = 0
        for letter in my_handle:
            if letter in twitter_handles[i]:
                score += 1  # we find similar letter, +1 to score
            else:
                score -= 1
        # add twitter_handle(as key), and score(as value) to scores dictionary
        scores[twitter_handles[i]] = score
    return scores


print(similiary_score('at', ['cat', 'dog']))


def suggestions(my_handle, twitter_handles, k):
    similarity_scores = similiary_score(my_handle, twitter_handles)
    similarity_counter = Counter(similarity_scores)
    top_suggestions = similarity_counter.most_common(k)
    return top_suggestions


print(suggestions('iLoveDogs', ['iLovedDoggo', 'ilovecat', 'button'], 2))
# Fill top k scores variable w/ first k keys
# If a value is great than whats in top scores variable, replace it

# Return top k handle names (keys)

# print(suggest('iLoveDogs', ['iLoveDog', 'iHateCat'], 1))

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
