# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

def create_phone_number(number):
  f = "".join(map(str,number[:3]))
  s = "".join(map(str,number[3:6]))
  t = "".join(map(str, number[6:10])) 

  return "(" + f + ") " + s + "-" + t


def create_phone_number_v2(number):
  return  "({}{}{}) {}{}{}-{}{}{}{}".format(*number)

print(create_phone_number([9,1,4,5,6,7,8,9,0,1])) # (914) 567-8901

print(create_phone_number_v2([9,1,4,5,6,7,8,9,0,1])) # (914) 567-8901
