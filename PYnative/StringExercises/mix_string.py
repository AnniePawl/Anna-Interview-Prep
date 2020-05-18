# Given 2 strings, return new string made of first, middle, and last char of each input string 

def mix_string(s1,s2):
  return s1[0] + s2[0] + s1[len(s1)//2] + s2[len(s2)//2 ] + s1[-1] + s2[-1]


print(mix_string("America", "Japan")) #AJrpan
print(mix_string("DOG", "plushy")) #DpOsGy