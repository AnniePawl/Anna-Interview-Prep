# You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.


def goal_parser(s):
  res = ""
  i = 0  
  while i < len(s):
    if s[i] == 'G':
      res += 'G'
      i+=1
    elif s[i] == "(":
      if s[i+1] == ")":
        res += 'o'
        i +=2
      else:
        res += 'al'
        i += 4
  return res





print(goal_parser('G()(al)')) # Goal
print(goal_parser("(al)GG(al)()()G")) # alGalooG

