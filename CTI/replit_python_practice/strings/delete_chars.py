# Given a string, delete all chars whose indices are divisible by 3 

def delete_chars(str):
  new_string = ""
  for i in range(len(str)):
    if i % 3 != 0:
      new_string += str[i]
  return new_string


def delete_chars2(str):
  new_string = ""
  for i, char in enumerate(str):
    if i % 3 != 0:
      new_string += char
  return new_string

print(delete_chars("python")) #yton
print(delete_chars2("python")) #yton