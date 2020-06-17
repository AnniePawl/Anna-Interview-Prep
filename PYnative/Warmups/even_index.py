# Print characters in string that are at even index 

def even_index(str): 
  result = ""
  for i in range(len(str)):
    if i % 2 ==0:
      result += str[i]
  return result 

def even_index2(str):
  for i in range(1,len(str)-1, 2):
    print(str[i])


print(even_index("pynative")) # pntv [0,2,4,6]

print(even_index2("pynative")) # pntv [0,2,4,6]