# Given a word, split it in two and reverse halves 
# If uneven word, attach middle letter to 1st chunk 


def two_halves(str):
  if len(str) % 2 == 0:
    return str[len(str)//2:] + str[:len(str)//2]
  else:
    return str[len(str)//2 +1:] + str[:len(str)//2+1]

print(two_halves("bear")) # arbe
print(two_halves("scrub")) # ubscr