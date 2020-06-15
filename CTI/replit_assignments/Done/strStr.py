# Return index of first occurance of needle in a haystack. Indec -1 if not in haystack. 

def strStr(needle, haystack):
  return haystack.find(needle) 

print(strStr("ll", "hello")) # 2
print(strStr("bba", "aaaa")) # -1

