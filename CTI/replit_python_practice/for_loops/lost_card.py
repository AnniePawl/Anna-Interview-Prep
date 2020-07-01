# Given set of cards from 1 to N, return card that's missing. 
# N is followed by N-1 integers 

a = int(input())
cards = []
for i in range(a-1):
  cards.append(int(input()))
cards.sort()

print(x for x in range(cards[0], cards[-1]+1) if x not in cards)

print(sorted(set(range(cards[0], cards[-1])) - set(cards)) )