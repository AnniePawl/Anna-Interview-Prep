# Given string, cap letters that occupy even indexes

def alternate_caps(string):
  new_string1 = ""
  new_string2 = ""
  for i in range(len(list(string))):
    if i % 2 == 0:
      new_string1 += string[i].upper()
      new_string2 += string[i]
    else: 
      new_string1 += string[i]
      new_string2 += string[i].upper()
  return [new_string1,new_string2]

def alternate_caps2(string):
  s = "".join(c if i%2 else c.upper() for i, c in enumerate(string))
  return [s,s.swapcase()]

def alternate_caps3(string):
  result = ["",""]
  for i, char in enumerate(string):
    result[0] += char.lower() if i % 2 else char.upper()
    result[1] += char.upper() if i % 2 else char.lower()
  return result


print(alternate_caps("codewars")) # [CoDeWaRs, cOdEwArS]
print(alternate_caps2("codewars")) # [CoDeWaRs, cOdEwArS]
print(alternate_caps3("codewars")) # [CoDeWaRs, cOdEwArS]