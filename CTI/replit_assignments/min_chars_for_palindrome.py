# Given a string, only operation allowed is insert chars at beginning of string 
# Return num of chars needed to make string a palindrom 

def min_chars(chars):
  count = 0
  chars_list = list(chars)
  middle = len(chars) // 2
  # base case 
  if chars_list == chars_list[::-1]:
    return count 
  else:
    chars_list.insert(0,chars[middle])
    count +=1
    min_chars(chars_list)
   

print(min_chars("ABA")) # 0
print(min_chars("AB")) # 1
print(min_chars("ABC")) # 2
print(min_chars("AACECAAAA")) # 2