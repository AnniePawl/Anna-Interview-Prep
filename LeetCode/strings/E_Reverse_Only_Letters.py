# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

# Pseudocode 
# Convert str to list to access by index and make swaps 
# Use 2 pointers to traverse str forwards and backwards 
# if chars at index are both letters --> swap them 
# if char is not alpha, move pointer 
# return list joined back into str

def reverse_letters(str):
  str = list(str)
  i = 0 #pointer 1 starts at beginning 
  j = len(str)-1 #pointer 2 starts at end 
  while i < j: #traverse until reach middle
    if str[i].isalpha() and str[j].isalpha(): # check if alpha
      str[i],str[j] = str[j],str[i] # swap 
      # move pointers along
      i+=1
      j-=1
    elif not str[i].isalpha():
      i +=1 #move pointer 
    elif not str[j].isalpha():
      j -=1 
    
  return "".join(str)
  



print(reverse_letters("ab-cd")) # "dc-ba"
print(reverse_letters("a-bC-dEf-ghIj")) #"j-Ih-gfE-dCba"
print(reverse_letters("Test1ng-Leet=code-Q!")) #"Qedo1ct-eeLg=ntse-T!"