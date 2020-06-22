# Given 5 intergers, print least of them  

least = int(input())

new_integer = int(input())
if new_integer < least:
  least = new_integer

new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
new_integer = int(input())
if new_integer < least:
  least = new_integer
  
print(least)