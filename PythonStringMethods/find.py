# find(value, start, end)
# Finds first occurange of specified value 
# Returns -1 if value not found 
# Almost the same as index() method, except index() raises exception if value is not found 


greeting = "hola como estas"
print(greeting.find("l")) # should return index of l --> 2
print(greeting.find("e")) # should return index of e --> 10
print(greeting.find("z")) # should return -1 to signify not found


# find() DOES NOT WORK ON  LISTS, but index() does
numbers = [1,2,3,4,5]
print(numbers.find(1))