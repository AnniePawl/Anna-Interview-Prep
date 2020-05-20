# Remove vowels from given string 

def remove_vowels(text):
  vowels = ["a","e", "i", "o","u"]
  for letter in text:
    if letter.lower() in vowels:
      text= text.replace(letter, "")
  return text
 

def short_cut(text):
  return ''.join(c for c in text if c not in 'aeiou')

  
print(remove_vowels("hohoho")) #hhh
print(remove_vowels("Anna")) # nn
print(remove_vowels("Happy Birthday")) #HppyBrthdys