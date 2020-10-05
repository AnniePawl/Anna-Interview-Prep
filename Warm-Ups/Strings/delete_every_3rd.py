# Given a string, delete all chars whose indice are divisible by 3 

def delete_3rd(str):
  new_str = ""
  for i in range(len(str)):
    if i % 3 != 0:
      new_str += str[i]
  return new_str

print(delete_3rd('Python')) #yton
print(delete_3rd('Anna')) #nn


def delete_3rd2(str):
  new_str = ""
  for i, char in enumerate(str):
    if i % 3 != 0:
      new_str += char
  return new_str
  
print(delete_3rd2('Good'))  # oo