# Given a string like "Code", return a string like "CCoCodCode"

def stringSplosion(s):
  splosion = ""
  for i in range(len(s)):
    splosion += s[:i+1]
  return splosion


print(stringSplosion("Code")) # CCoCodCode