# The power of the string is the maximum length of a non-empty substring that contains only one unique character. Return power
def consecutive_char(str):
  # check if len str == str.count(str[0])
  if len(str) == str.count(str[0]):
    return len(str)
  
  temp = 1 
  max = 0 
  for i in range(len(str)-1):
    if str[i] == str[i+1]:
      temp +=1 
    else:
      if temp > max:
        max = temp 
      temp = 1
  # deal w/ edge case last letter part of contiguous string
  return max 


# edge case all letters are the same 
print(consecutive_char("aaaa")) # 4  
print(consecutive_char("leetcode")) # 2
print(consecutive_char("abbcccddddeeeeedcba")) # 5
print(consecutive_char
# edge case last letter part of longest consecutive 
("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz")) # 8