# endswith(value, start,end) 
# value --> required 
# start --> optional integer specifying where to start search   
# end --> optional integer specifying where to end search 


txt = "Hell, welcome to my world."
x = txt.endswith("my world.")
print(x) # Should return boolean True

# Return True is a sting is end of b string or b string end of a string
def endsWith(a,b):
  return a.endswith(b) or b.endswith(a)

print(endsWith("abc","xyzabc")) # True 
print(endsWith("grunge","punk")) # False
print(endsWith("bag","doggybag")) # True 