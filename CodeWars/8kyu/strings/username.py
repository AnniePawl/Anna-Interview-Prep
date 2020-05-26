# Validate username 
# Allowed characters - lowercase letters, numbers, underscore 
# between 4 and 16 chars 


import re
def username(un):
    return re.match('^[a-z0-9_]{4,16}$', un) != None

print(username("anabanana")) # True
print(username("ab")) # False 
print(username("a_n_n_a")) # True
print(username("grettle5")) # True