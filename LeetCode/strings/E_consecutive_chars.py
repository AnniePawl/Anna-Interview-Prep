# The power of the string is the maximum length of a non-empty substring that contains only one unique character. Return power


def consecutive_char(s):
  max_count = 1
  count = 1
  if s.count(s[0]) == len(s):
    return len(s)

  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      count +=1 
    else: 
      if count > max_count:
        max_count = count
      count = 1
  return max_count

print(consecutive_char("aaaa")) # 4
print(consecutive_char("cc")) #2
print(consecutive_char("anna")) # 2     
print(consecutive_char("leetcode")) # 2
print(consecutive_char("abbcccddddeeeeedcba")) # 5
print(consecutive_char("aabbbbbccccdddddddeffffffggghhhhhiiiiijjjkkkkkllllmmmmmnnnnnoopppqrrrrsssttttuuuuvvvvwwwwwwwxxxxxyyyzzzzzzzz")) # 8