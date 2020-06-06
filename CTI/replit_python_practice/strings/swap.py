# Given two words separating by space ,print new string swith first and second words swapped. 

def swap(s):
  return " ".join(s.split(" ")[::-1])

print(swap("hello world")) # world hello
print(swap("hello,  world!")) # world!  hello,