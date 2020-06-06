# Given string, cut into equal parts. If off len, leave middle in first chunk. Print new string on single row w/ first and second halves swapped. 

def swap(str):
  length = len(str)
  if length % 2 == 0:
    return  str[length//2:] + str[:length//2]
  else: 
    return str[length//2 + 1:] + str[:length//2 +1 ]
  
def swap2(s):
  mid = (len(s) + 1) //2 
  return (s[mid:] + s[:mid])

print(swap('Qwerty')) # rtyQwe
print(swap('annaP')) # aPann

print(swap2('Qwerty')) # rtyQwe
print(swap2('annaP')) # aPann


