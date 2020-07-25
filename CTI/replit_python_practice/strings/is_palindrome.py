# Given a string, print "Palindrome" if it's a palindrome. Otherwise print "Not Palindrome"


def is_palindrome(str):
  if str == str[::-1]:
    return "Palindrome"
  return "Not Palindrome"

print(is_palindrome("ABBA")) # Palindrome
print(is_palindrome("Python")) # Not Palindrome