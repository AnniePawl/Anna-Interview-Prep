# index()
# returns index of first occurances of specified value 
# Very similar to find() except will return error instead of -1 if not found


# index() works on LISTS, but find() does not
numbers = [1,2,3,4,5]
print(numbers.index(1)) # 0
print(numbers.index(3)) # 2


greeting = "hola como estas"
print(greeting.index("l")) # should return index of l --> 2
print(greeting.index("e")) # should return index of e --> 10
print(greeting.index("z")) # should return ERROR


