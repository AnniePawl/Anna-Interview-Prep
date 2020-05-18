# join()
# Takes all items in iterable and joins them 
# Can't join



# This joings all items in dictionanry using work TEST as separator 
my_dictionary = {"name":"patty", "country":"norway"}
mySeparator = "TEST"

x = mySeparator.join(my_dictionary)
print(x)


# Can use on lists, strings, tuples 

# Combines list items into single string
# " " before join is called seperator 
print(" ".join(["This", "is", "a", "string"]))
print(" ".join(['Tiger', 'Lily']))
print(" ".join(('Lily', 'Pad')))
# Will iterate over every letter and separate w/ "-"
print("-".join('Missippippi')) # M-i-s-s-i-p-p-i

print(".".join("bfg").upper()) # B.F.G




# ERRORS
# print("".join("This", "is"))

