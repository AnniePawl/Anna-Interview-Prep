# Given a word that may contain "p", return index of second occurance. Return -1 if second occurance doesn't exist


def second_occurance(word):
  first_p = word.find('p')
  if word.count("p") < 2:
    return -1
  else:
    return word.find('p', first_p + 1)

    
print(second_occurance("appropriate")) # 2 
print(second_occurance("puppet")) # 2 
print(second_occurance("spare")) # -1 