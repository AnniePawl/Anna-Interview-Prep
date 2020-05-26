# Reverse words in string 

def reverse(str):
  return " ".join(str.split(" ")[::-1])

print(reverse("how now brown cow")) # cow brown now how