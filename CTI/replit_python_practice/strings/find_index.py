#  Print index of first and last offurance of 'f'. If 'f' only appears once, just print 1 index. If 'f' doesn't occur, print -1

def find_index(s):
  if s.count('f') == 1:
    print((s.find('f')))
  elif s.count('f') > 1:
    print( s.find('f') , s.rfind('f'))
  else:
    print( -1)
  

# Solution 
s = input()
if s.find('f') == s.rfind('f'):
  print(s.find('f'))
else:
  print(s.find('f'), s.rfind('f'))

  
print(find_index("comfort")) # 3
print(find_index("office")) # 1 2
print(find_index("hello")) # -1