# capitalize()
# converts first letter into uppercase 

name = "gretta goodspeed"
print(name.capitalize()) # Gretta goodspeed

# title()
# converts first char of each word to uppercase
name = "gretta goodspeed"
print(name.title()) # Gretta Goodspeed

# casefold()
# returns string where all characters are lower case 
# similar to lower(), but stronnger --> meaning it will convert more chacters to lower? 

string = "ghfGhdUN"
print(string.casefold())

# lower()
# returns string where all characters are lowercase 
string = "ghfGhdUN"
print(string.lower())

# swapcase()
# converts upper to lower and vice versa 
swap = "bOOt"
print(swap.swapcase()) # BooT

# upper()
# converts all characters to uppercase 
bfg = "b.f.g"
print(bfg.upper())

# istitle()
# returns true if string follows title rules 
print("Harry Potter".istitle()) # True 
print("Harry potter".istitle()) # False

# isupper()
# returns True if all characters are uppercase 
print("bgf".isupper()) # False 
print("BFG".isupper()) # True

# islower()
# returns True if all characters are lowercase 
print("bgf".islower()) # True 
print("BFG".islower()) # False
print("b.f.g".islower()) # True 


