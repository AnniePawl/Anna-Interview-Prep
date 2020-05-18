# Find all occurances of USA. Return count 

def count_usa(str):
  return str.lower().count("usa")

def count_usa2(str):
  count = 0 
  for i in range(len(str)):
    if str.lower()[i:i+3] == "usa":
      count +=1
  return count
  

print(count_usa("Welcome to USA. usa is awesome")) #2

print(count_usa2("Welcome to USA. usa is awesome")) #2