# Create an outer function that accepts a and b. Create inner function that calculates their sum. Add 5 to outer function 

def outerFun(a, b):
    square = a**2
    def innerFun(a,b):
        return a+b
    add = innerFun(a, b)
    return add+5

result = outerFun(5, 10)
print(result)