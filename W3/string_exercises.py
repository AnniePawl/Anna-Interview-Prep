s = "I do Not like Green eggs and Ham"
s2 = 'how Now brown Cow'

# 1. Find len of string 
def length(s):
  return len(s)

print(length(s)) # 32

# 2. Find frequency of all chars in a string 
def char_frequency(s):
  frequencies = {}
  s = s.lower()
  s = s.replace(' ', '')
  for char in s:
    if char in frequencies:
      frequencies[char] +=1
    else:
      frequencies[char] = 1
  return frequencies

print(char_frequency(s))

# 3. Return new string made of first 2 and last 2 chars of a string 
def first_last(s):
  return s[:2] + s [-2:]

print(first_last('butternut')) # buut

# 4. Return a string where all occurances of it's first char are changed to '$' except first char 
def cash(s):
  s = s[0] + s[1:].replace('r','$')
  return s
  
print(cash('restart reboot')) #resta$t $eboot

# 5. Turn two strings into single string seprated by space w/ first char of each string swapped 
def combine_swap(s1,s2):
  s3 = s2[0] + s1[1:] + ' ' + s1[0] + s2[1:]
  return s3

print(combine_swap('abc', 'xyz')) # xbc ayz

# 6. Add 'ing' to end of string. If string already has 'ing', add, 'ly
def ing(s):
  if s.endswith('ing'):
    s += 'ly'
  else:
    s += 'ing'
  return s

print(ing('string')) #stringly
print(ing('play')) #playing

# 8 Return longest word and it's len 
def longest(s):
  longest = ""
  count = 0
  for word in s.split():
    if len(word) > len(longest):
      longest = word 
      count = len(word)
  return longest, count
  
print(longest(s))

# 9. Remove nth char from string 
def remove_nth(s,n):
  return s[:n] + s[n+1:]

print(remove_nth('ginger', 2)) #giger

# 10. Exchange first and last chars 
def swap(s):
  return s[-1] + s[1:-1] + s[0]
  
print(swap('hello')) # oellh

# 11. Remove chars w/ off index values in string 
def remove_odds(s):
  result = ""
  for i in range(len(s)):
    if i % 2 == 0:
      result += s[i]
  return result 


print(remove_odds('howdy')) # hwy

# 12. Count occurance of each word in sentence
def word_occurance(s):
  histo = {}
  for word in s.split():
    if word in histo:
      histo[word] += 1 
    else:
      histo[word] = 1
  return histo

print(word_occurance('the cat the hat the bat'))

# 13. / 

# 14. / 

# 15. Wrap tag around word 
def tag(tag, str):
  return "<" + tag + ">"  + str + "</"  +tag + ">"
  
print(tag('li', 'item1s')) # <li>tag</li>

# 16. Insert s2 in middle of s1
def middle(s1, s2):
  return s1[:2] + s2 + s1[2:]

print(middle("{{}}", 'PHP')) # {{PHP}}

# 17. Return 4 copies of last 2 chars 
def repeat_end(s):
  return s[-2:] * 4

print(repeat_end('python')) # onononon

# 18. Return first 3 chars. If str less than 3, return original str
def first_three(s):
  return s[:3] if len(s) > 3 else s

print(first_three('python')) #pyt
print(first_three('go')) #go

# 19. / 

# 20. Return reversed str if length is multiple of 4 
def reverse_4(s):
  if len(s) % 4 == 0:
    return s[::-1]
  return s

print(reverse_4('hell')) #lleh
print(reverse_4('hello')) #hello
print(reverse_4('papercut')) #tucrepap

# 21. If str has at least 2 uppercase in first 4 chars, return all caps. 
def caps(s):
  count = 0
  for letter in s[:4]:
    if letter.isupper():
      count +=1
  if count >= 2:
    return s.upper()
  return s

print(caps('Anna')) # Anna
print(caps('GOfish')) # GOFISH

# 22. Lexigraphically sort stringg 
def lex_sort(s):
  return sorted(s, key=str.upper)

print(lex_sort('gAhyCs'))


# 23. Remove new line from end of string 
def remove_new_line(s):
  return s.rstrip()

print(remove_new_line('Python Exercises\n'))

# 24. Check if str strat wtih specified chars 
def starts_with(s1,s2):
  return s1.lower().startswith(s2.lower())

print(starts_with('Anna', 'an')) # True 
print(starts_with('Anna', 'pn')) # False

# 25. See caesar_cipher.py

# 26. Display formatted text w/ 10 char width  
# import textwrap

# 27. Remove all indentation from str
# import textwarp

# 28. Add prefix to each str 
# import textwrap

# 29. Set indentation 

# 30. Return floating number up to 2 decimal places 
def twodec(num):
  print(type('{:.2f}'.format(num))) #this returns a string
  return float('{:.2f}'.format(num)) #this returns a string

print(twodec(3.141592)) # 3.14

# 31. float w/ sign 

# 32. Return float w/ no decimal places 
def nodec(num):
  return '{:.0f}'.format(num)
  
print(nodec(3.141592)) # 3
print(nodec(3.9)) # 4

# 33. print int w/ specified zeros on left 
#  you can use format or .zfill. This only works on strings
def zeros(num):
  print(str(num).zfill(3))
  print(f'{num:05d}')
  return '{:03d}'.format(num) # will pad w/ 1 zero 
  # need to account for original width

print(zeros(15)) # 00015

# 34. Add 3 stars to right on int 
def add_stars(num):
  return f'{num:*<4d}'

print(add_stars(5)) # 5***

# 35. Add commas to value 
def commas(num):
  # print('{:,}'.format(num))
  return f'{num:,}'

print(commas(3000000)) #3,000,000

# 36. Format num w/ percentage 
# number before p% specified number of decimal places
def percentage(num):
  return f'{num:.0%}'

print(percentage(.25)) # 25%

# 37. format 

# 38. Count occurances of substring 
def substring2(s1,s2):
  return s1.count(s2)

print(substring2('annabannanna', 'an')) # 3

# 39. Reverse string 
def reverse(s):
  print(''.join(reversed(s)))
  return s[::-1]

# 40. Reverse words in a string 
def reverse_words(s):
  return ' '.join(s.split(' ')[::-1])

print(reverse_words('hansel and grettle')) # grettle and hansel

# 41. Strip set of chars from string 
def string_chars(s1,s2):
  return "".join(letter for letter in s1 if letter not in s2)

print(string_chars('otter bot', 'o')) # tter bt