# Given a num, return odd or even 

def odd_even(num):
  if num %  2 == 0:
    return 'even'
  else:
    return 'odd'

print(odd_even(5)) # odd
print(odd_even(10)) # even