# Given a string, compress it by shortening sequence of same char to char followed by number of repetitions.  (Run Length Encoding)

# Using a dict won't work b/c you're only counting consecutive chars. See test case 4
def compression(s):
  compression = ""
  sum = 1
  for i in range(len(s)-1):
    if s[i] == s[i+1]:
      sum +=1 
    else:
      compression += s[i] + str(sum)
      sum = 1
  compression += s[i] + str(sum)
 
  return compression

  
 
  



  

# Test Cases
print(compression('a')) # a
print(compression('aaa')) # a3
print(compression('abbccc')) # a1b2c3
print(compression('abbccc')) # a1b2c3
print(compression('abbcccaaaa')) # a1b2c3a4