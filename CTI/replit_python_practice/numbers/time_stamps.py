# Given two timestamps of the same day: a number of hours, minutes and seconds for both of the timestamps. The moment of the first timestamp happened before the moment of the second one. Calculate how many seconds passed between them.


# Read an integer:
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
seconds1 = (a * 60**2 + b * 60 + c)
seconds2 = (d * 60**2 + e * 60 + f)
# Print a value:  
print(seconds2 - seconds1)
