
# strip() --> removes all leading and trailer characters
# lstrip(characters) --> removes specified leading characters to left 
# rstrip(characters) ---? removes specidied leading characters from right

question = "?????WHAT?????" 
print(question.strip("?")) # WHAT

question1 = "?????WHAT?????"
print(question1.lstrip("?"))  # WHAT?????

question2 = "?????WHAT?????"
print(question2.rstrip("?"))  # ?????WHAT

hypthen = "-m-i-s-s-i-p-p-i-"
print(hypthen.strip("-")) # "m-i-s-s-i-p-p-i"


spaces =  "    bannana     "
print(spaces.strip())
print(spaces.rstrip())



