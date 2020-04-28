# Given 2 strings, a and b, return number of positions where they contain the same length 2 substrings.


def string_match(a, b):
  # Figure out which string is shorter
  shorter = min(len(a), len(b))
  count = 0 # initialize a count var

  # Use len-1 so you can use char str[i+1] in loop for i in range(shorter-1)
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count +=1
  return count



print(string_match('xxcaazz', 'xxbaaz'))  # 3
print(string_match('abc', 'abc'))  # 2
print(string_match('abc', 'axc'))  # 0
