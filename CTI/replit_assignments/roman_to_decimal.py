def roman_to_decimal(roman_numeral):
  arabic_numeral = 0
  i = 0
  while (i < len(roman_numeral)): 
    # Getting value of symbol s[i] 
    s1 = value(roman_numeral[i])
    if (i+1 < len(roman_numeral)):
      # Getting value of symbol s[i+1] (the next number)
      s2 = value(roman_numeral[i+1])
      # Comparing both values 
      if (s1 >= s2): 
        pass # when you see "pass", replace it with your code
        # Value of current symbol is greater 
        # or equal to the next symbol 
      else: 
        pass # when you see "pass", replace it with your code
        # Value of current symbol is less than 
        # the next symbol 
    else:
      pass # when you see "pass", replace it with your code
  
    return arabic_numeral 

  
# Helper Function 
def value(roman_char):
  if roman_char == "I":
    return 1 
  if roman_char == "V":
    return 5
  if roman_char == "X":
   return 10
  if roman_char == "L":
   return 50
  if roman_char == "C":
   return 100
  if roman_char == "D":
   return 500
  if roman_char == "M":
   return 1000
  return -1

print(value())

# def value(r): 
#     if (r == 'I'): 
#         return 1
#     if (r == 'V'): 
#         return 5
#     if (r == 'X'): 
#         return 10
#     if (r == 'L'): 
#         return 50
#     if (r == 'C'): 
#         return 100
#     if (r == 'D'): 
#         return 500
#     if (r == 'M'): 
#         return 1000
#     return -1





  