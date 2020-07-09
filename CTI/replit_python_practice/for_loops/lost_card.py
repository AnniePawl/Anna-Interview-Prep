# Given set of cards from 1 to N, return card that's missing. 
# N is followed by N-1 integers 


# Set strategy 
a = int(input())
all_cards  = set(x for x in range(1,a+1))
cards = set()
for i in range(a-1):
  cards.add(int(input()))

print(all_cards.difference(cards))


# Sum / subtraction strategy 
n = int(input())
cards_sum = 0 
for i in rannge(1,n +1):
  cards_sum + i 
for i in range(n-1):
  cards_sum -= int(input()):
print(cards_sum)