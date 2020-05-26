# Take in size and return string of alternative 1s and os starting w/ 1 

def stringy_string(size):
  string = ""
  for i in range(size):
    if i % 2 == 0:
      string += "1"
    else:
      string += "0"
  return string
    
def stringy_string2(size):
  return "".join([str(i%2) for i in range(1, size+1)])


print(stringy_string(4)) #1010
print(stringy_string(8)) #10101010

print(stringy_string2(4)) #1010
print(stringy_string2(8)) #10101010