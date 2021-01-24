# 80. Count number of substrings w/ same first and last chars 

def count_substrings(s):
  result = 0 
  for i in range(len(s)):
    for j in range(i,len(s)):
      if s[i] == s[j]:
        result += 1
  return result 


print(count_substrings('abc')) # 3
print(count_substrings('abbc')) # 5
print(count_substrings('abbcb')) # 7