## Assignment Two: Twitter Follow Suggestions 
Improve suggestions for accounts to follow. Implement a function that accepts a new user's handle and an array of many other user's handles. Calculate a similartity score between a pair of handles by looking at the letters each contains. Score +1 for each letter in alphabet that occurs in both handles. Score -1 for each lettr that occurs in only onle handle. Your function should return K handles from array that has highest similarly score to new user's handle.

```python
from collections import Counter

def similiary_score(my_handle, twitter_handles):
    scores = {} # keep track of a score
    # create a loop to compare letters in my_handle to letters in each twitter_handle
    for i in range(len(twitter_handles)):
        score = 0
        for letter in my_handle:
            if letter in twitter_handles[i]:
                score += 1  # if we find similar letter, +1 to score
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
```