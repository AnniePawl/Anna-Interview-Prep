# 76. Count number of substrings with exactly k distinct chars 


# Brute Force Method 
# O(n^3) BAD 
# Generate all substrings, then check if each one has exactly k distinc chars 
def distinct_substring(s, k):
  count = 0
  # Generate all substrings of len k 
  substrings = []
  for i in range(len(s)-(k-1)):
    substrings.append(s[i:i+k])
  # Check if each substring contains unique chars 
  for subsub in substrings:
    subletters = [letter for letter in subsub]
    if len(subletters) == len(set(subletters)):
      count +=1
  return count

print(distinct_substring('wolf', 4)) # 1 
print(distinct_substring('anna', 3)) # 0 
print(distinct_substring('anna', 2)) # 2 
