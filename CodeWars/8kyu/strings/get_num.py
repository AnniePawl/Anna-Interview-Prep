# Return number from string 

def get_num(string):
  num_list = [num for num in string if num.isdigit()]
  return int("".join(num_list))



print(get_num("12")) #12
print(get_num("my fave num is 7")) # 8
print(get_num("he1100 w0r1d")) # 110001