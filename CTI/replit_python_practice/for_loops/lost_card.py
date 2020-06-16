# Given set of cards from 1 to N, return card that's missing. 
# N is followed by N-1 integers 

def missing_card(nums):
  number_of_cards = nums[0]
  remaining_cards = nums[1:]
  all_cards = list(range(1,number_of_cards+1))
  for num in all_cards:
    if num not in remaining_cards:
      return num

print(missing_card([5,3,5,2,1])) # 4