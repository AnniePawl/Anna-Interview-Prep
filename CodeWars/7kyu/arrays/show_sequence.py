# Given an int, compute series starting from 0 and ending at given num. Show sequence adn sum in a string output 


# Brute Force 
# This only works for nums <10 b/c .join separates all nums 
def show_sequennce(n):
  sum = 0 
  string = ""
  # Base cases 
  if n == 0:
    return "0=0"
  if n<0:
    return str(n) + "<0"
  else:
    for num in range(0,n +1):
      sum += num 
      string += str(num)
  return "+".join(string) + " = " + str(sum) 

def show_sequennce2(n):
  sum = 0 
  string = ""
  # Base cases 
  if n == 0:
    return "0=0"
  if n<0:
    return str(n) + "<0"
  else:
    for num in range(0,n +1):
      sum += num 
      string += str(num) + "+"
  return string[:-1] + " = "  + str(sum) 

# Using counter
def show_sequennce3(n):
    if n == 0:
        return "0=0"
    elif n < 0:
        return str(n) + "<0"
    else:
        counter = sum(range(n+1))
        return '+'.join(map(str, range(n+1))) + " = " + str(counter)


print(show_sequennce(4)) # "0+1+2+3+4 = 10"
print(show_sequennce(6)) # "0+1+2+3+4+5+6 = 21"
print(show_sequennce(-10)) # "-10<0"
print(show_sequennce(0)) # "0=0"
print(show_sequennce(12)) # "0=0"


print(show_sequennce2(4)) # "0+1+2+3+4 = 10"
print(show_sequennce2(6)) # "0+1+2+3+4+5+6 = 21"
print(show_sequennce2(-10)) # "-10<0"
print(show_sequennce2(0)) # "0=0"
print(show_sequennce2(12)) # "0=0"

print(show_sequennce3(4)) # "0+1+2+3+4 = 10"
print(show_sequennce3(6)) # "0+1+2+3+4+5+6 = 21"
print(show_sequennce3(-10)) # "-10<0"
print(show_sequennce3(0)) # "0=0"
print(show_sequennce3(12)) # "0=0"