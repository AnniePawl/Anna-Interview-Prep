# Convert name into initials 

def abbrevName(name):
  name_string = name.split(" ")
  return name_string[0][0].upper() + "." + name_string[1][0].upper()


def abbrevName2(name):
  first, last = name.upper().split(" ")
  return first[0] + "." + last[0]

def abbrevName3(name):
  return ".".join(w[0] for w in name.split()).upper()

print(abbrevName("Anna Pawl")) # A.P
print(abbrevName("kit harrington")) # K.H
print(abbrevName("Harry potter")) # H.Psga