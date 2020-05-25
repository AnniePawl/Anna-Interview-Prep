# Given string and int, return new string split into parts accoding to int 

def split_string(str, split):
  new_string = ""
  for i in range(0,len(str),split):
    new_string += str[i:i+split] + " "
  return new_string[:-1]

# One-liner 
def split_string2(str,split):
  return " ".join([str[i:i+split] for i in range(0,len(str), split)])


print(split_string("hotdoggod", 3)) # hot dog god
print(split_string("dog", 1)) # d o g 


print(split_string2("hotdoggod", 3)) # hot dog god
print(split_string2("dog", 1)) # d o g 

