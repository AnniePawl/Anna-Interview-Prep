# Convert String to Integer 
# Discards whitespace and interprets at first non-white space character (.strip())
# If first non-white space is string, no converstion, return 0
# Else, deal w/ optional '+' or '-' (str[0])
# If  number our of 32 bit signed range, return int max or min


def atoi(s):
  sign = 1
  s = s.strip() # get rid of whitespace 
  if s[0] not in "+-0123456789": 
    return 0
  if s[0] == "-":
    sign = -1

  i = 0 
  result = ""
  while i < len(s) and s[i].isdigit():
    result +=s[i]
  return int(result)*sign


print(atoi(" 42")) # 42
print(atoi("   -42")) # -42
print(atoi("4193 with words")) # 4193
print(atoi("words and 987")) # 0 b/c first non-whitespace is str
# print(atoi("-91283472332")) # -2147483648 b/c out of range so INT_MIN (−231) returned 