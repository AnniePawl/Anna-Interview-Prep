# Given array of ints, check if any are character codes for lower case (a,e,i,o,u). If so, chage that value to string of that vowel

def is_vowel(nums):
  return [char(n) if char(n) in "aeiou" else n for n in nums]
