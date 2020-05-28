# string.format(value1, value2)
# formats specified values and inserts them inside string's placeholder. 
# Placeholders can be identified inside '{}'

greeting = "hello {}, your {} looks great today.".format("gretta", "hair")
print(greeting)

age = "She is {age} years old".format(age=100)
print(age)

# Modulus
# You can also use modulo operator to format string- in this case, you can omit '.format()' at end


# formatting type 
# Insde plceholder you can format result  