# Given string that may contain 'p', print index of second occurance. If only occurs once, print -1. If no p, print -2 

def p_index(s):
  first_p = s.find('p')
  if 'p' not in s:
    return -2
  elif s.count('p') == 1:
    return -1 
  else:
    return s.find('p', first_p + 1)


# CTI Solution 
s = input()
if 'p' in s:
  if s.find('p') == s.rfind('p'):
    print(-1)
  else:
    print(s.find('p') + s[s.find('p') + 1:].find('p') + 1)
else:
  print(-2)
  
print(p_index('ppppp')) # 1
print(p_index("appropriate")) # 2 
print(p_index("spare")) # -1 
print(p_index("reason")) # -2 