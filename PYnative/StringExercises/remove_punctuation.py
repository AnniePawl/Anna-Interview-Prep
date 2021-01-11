# Remove special symbols & punctuation
import string 

def remove_punctuation(s):
  return s.translate(str.maketrans('', '',string.punctuation))
  
print(remove_punctuation("/*Jon is @developer & musician"))
# “Jon is developer musician”

