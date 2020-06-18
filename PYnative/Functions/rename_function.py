# Assign different name to function and call if thru new name 

def displayStudent(name, age):
  print(name, age)

showStudent = displayStudent
showStudent("Boo", 11)