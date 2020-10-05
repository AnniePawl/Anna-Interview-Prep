# Given a string,  return either 'palindrome' or 'not palindome'

def is_palindrome(str):
  if str == str[::-1]:
    return 'palindrome'
  else:
    return 'not palindrome'

print(is_palindrome('anna')) #palindrome
print(is_palindrome('annapawl')) # not palindome