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

# 42. Count repeated chars in a string 
# make a dict of char occurances, then iterate over dictoionary. if letter appears more than once, print it 
def repeat(str):
  histo = {}
  for letter in str:
    if letter in histo:
      histo[letter] += 1
    else:
      histo[letter] =1
  
  for key, value in histo.items():
    if value > 1:
      print(key, value)

print(repeat('thequickbrownfoxjumpsoverthelazydog'))

# 43. Print square and cube symbol in area of 

# 44. Print indx of char in str
def i(str, char):
  return str.index(chars)

# 45.  CHeck if a string contains all letters of alphabet 

# 46. Convery String into list 
def string_list_word(str):
  return list(str)

def string_list_sentence(str):
  return str.split(' ')

print(string_list_word('anna')) # [a,n,n,a]
print(string_list_sentence('anna is cool')) # [anna, is, cool]


# 47. Convery first n chars to lowercase 
def first_n_lower(str, n):
  return str[:3].lower() + str[3:]

print(first_n_lower('ANNAISCOOL', 4)) #annAISCOOL


#48. Swap comma and dot in str 
# Replace will only swap one for another 
# Use translate() to deal with two swaps
def swap_chars(str):
  maketrans = str.maketrans
  str = str.translate(maketrans(',.', '.,'))
  return str

print(swap_chars('A.D,')) # A,D.

# 49. Count and display vowels from given text 
def count_vowels(str):
   # str? 
  counts = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
  for letter in str:
    if letter in counts:
      counts[letter] +=1 
  
  for key, value in counts.items():
    print(key, value)

print(count_vowels('anna is even oranger')) # {a:3, e:2, i:1, o: 1, u:0}


# 49.5 Return total count of vowels in a string
def count_vowels2(str):
  vowels = 'aeiou'
  return sum(1 for letter in str if letter in vowels)
  # return len([letter for letter in str if letter in vowels])

print(count_vowels2('anna is even oranger')) # {a:3, e:2, i:1, o: 1, u:0}

# 50. Split string on last occurance of delimeter
def split(str, delimeter):
  return str.rsplit(delimeter, 1)

print(split('1,2,3,4,5', ',')) # ['1,2,3,4', '5']

# 51. Find first non repearting char in given string  
def non_repeating(str):
  freqs = {}
  for letter in str:
    if letter in freqs:
      freqs[letter] += 1 
    else:
      freqs[letter] = 1 
   
  for letter in freqs:
    if freqs[letter] == 1:
      return letter
  return 'all letters repeat'
  


print(non_repeating('aaabbcdd')) # c
print(non_repeating('aaabbccaffgg')) # all letters repeat 


# 52. Print all permutations with given repetition number of chars in given string


# 53. Find first repeated char in given string 
# See repeated_chars.py

# 54. Find first repeated char where index of first occurance is smallest 

# 55. First repeated word in str 

# 56. Second most repeated word in str
def second_most_repeated(str):
  counts = {}
  for letter in str.split():
    if letter in counts: 
      counts[letter] += 1 
    else:
      counts[letter] = 1 
  
  return(sorted(counts.items(), key = lambda kv: kv[1]))[-2][0]
  


print(second_most_repeated('ab ba ba ab ba cd')) # ab

# 57. Remove spaces from string 
def remove_spaces(str):
  return str.replace(' ','')

print(remove_spaces('hi there sweets')) # 'hitheresweet

# 58. remove spaces from front of string 
def front_space(str):
  return str.lstrip()
print(front_space('   anna')) #anna

# 59. Find max occuring char 
def max_occuring(str):
  counts = {}
  for letter in str.replace(' ',''):
    if letter in counts:
      counts[letter] +=1
    else:
      counts[letter] = 1 

  return sorted(counts.items(), key=lambda kv:kv[1])[-1][0]

def max_occuring2(str):
  counts = {}
  for letter in str.replace(' ',''):
    if letter in counts:
      counts[letter] +=1
    else:
      counts[letter] = 1 

  return max(counts, key=counts.get)


print(max_occuring('hi my name is bob and i like cats'))
print(max_occuring2('hi my name is bob and i like cats'))

# 60. Capitalize first and last letter of each word in str 
def cap_first_last(str):
  result = ""
  for word in str.split():
    result += word[0].upper() + word [1:-1] + word[-1].upper() + " "  
  return result


print(cap_first_last('anna is cool')) # AnnA IS CooL

# 61. Remove duplicate chars 
def remove_dups(str):
  # doesnt return in order 
  # return ''.join(set(str))
  return ''.join(dict.fromkeys(str)) # returns in order
  

print(remove_dups('butter')) #buter

# 62. Compute sum of digits in given string 
# this sums individial digits but doesnt account for digits next to eachother 
def sum_str_digits(str):
  digits = [int(char) for char in str if char.isdigit()]
  return sum(digits)

# accounts for digits next to eachother
def sum_str_digits2(str):
  temp = '0'
  digits = []
  for i in range(len(str)):
    if str[i].isdigit():
      temp += str[i]
    else:
      digits.append(temp)
      temp = '0'
  # Add whatever remains in temp to account for last char in str being digit 
  return sum(int(digit) for digit in digits) + int(temp)


print(sum_str_digits('1gh3io22j')) # 26
print(sum_str_digits2('123a')) # 123
print(sum_str_digits2('1gh3io22j')) # 26
print(sum_str_digits2('1gh3io22j3')) # 29

# 63. Remove leading zeros from IP address 

# 64. Find max len of consecutive 0's in bianry string 
def max_zeros(str):
  temp = 0
  max = 0 

  for digit in str:
    if digit == '0':
      temp +=1
    else: 
      if temp > max:
        max = temp 
        temp = 0
  return max
 

print(max_zeros('1001100010')) # 3

# 65. Return common letters (in lexigraphical order) from 2 strings
def common_letters(s1,s2):
  return ''.join(sorted(set(s1).intersection(set(s2))))
  
print(common_letters('butterfly', 'baffle')) # befl

# 66. Return number of chars that need to be removed to make two strings anagrams 
# See two_string_anagram.py 

# 67. Write python program to remove all consecutive duplicates from string

# 68. Create two strings from given string. First string using cahrs that only occur once, second string from chars that occur multiple times 
# See 'two_strings.py'
def two_strings(s): # O(n^2)
  singles = ''
  dups = ''
  for char in s.replace(' ', ''): # O(n)
    if s.count(char) == 1: # O(n)
      singles += char
    else:
      if char in dups: # O(n)?
        continue 
      else:
        dups += char 

  return singles, dups

def two_strings2(s): # O(n)
  counts = {}
  for char in s.replace(' ',''): # O(n)
    if char in counts: # 0(1) to check if key in dict 
      counts[char] += 1
    else:
      counts[char] = 1

  singles = ''
  doubles = ''
  for key, value in counts.items():
    if value == 1:
      singles += key
    else:
      doubles += key

  return (singles, doubles)



print(two_strings('apple bottom jeans')) # 'lbmns' 'apeto'
print(two_strings2('apple bottom jeans')) # 'lbmns' 'apeto'

# 69. Longest Common substring
#  See longest_common_substring.py

# 71. Move all spaces to front of string in single traversal 
# V1 not in single traversal
def move_spaces(str):
  count = sum(1 for char in str if char == ' ')
  return ' '*count  + str.replace(' ', '')

print(move_spaces('i am a cat')) #'   iamacat'


# 72. Remove all chars except specified char from string 
def remove_all(str, x):
  return ''.join([char for char in str if char==x])

print(remove_all('google','g')) # gg


# 73. count uppercase and lowercase 
def count_upper_lower(s):
  upper = 0 
  lower = 0
  for letter in s:
    if letter.isupper():
      upper +=1 
    else:
      lower +=1 
  return 'Upper: ' + str(upper) + ' Lower: ' + str(lower)

print(count_upper_lower('Cat In The Hat')) 

# 76. Count substrings w/ exactly k distinct chars. 
#  See substrings_distinct_chars.py

# 77. Count non-empty substrings of given string
# Formula for calculating all substrings ? 

#  78. Count chars at same position in string as position in english alphabet 

# 79. Final smallest and largest word in str 
def smallest_largest(s):
  words = s.split()
  # note that min and max return first and last word alphabetically
  min = words[0]
  max = words[0]
  for word in words: 
    if len(word) > len(max):
      max = word 
    if len(word) < len(min):
      min = word 
  return min, max 

print(smallest_largest('how can i grow larger')) # i, larger

# 80. Count substrings w/ same first and last chars 
# See sub_string_first_last.py