# Return letters in reverse order 
def reverse(letters):
  reversed = ""
  for i in range(len(letters)-1, -1, -1):
    reversed += letters[i]  
  return reversed
 


print(reverse("AB")) # BA
print(reverse("EFG")) # GFE