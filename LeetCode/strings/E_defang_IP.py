# Defang IP address str by replacing "." with "[.]"

def defang(IP):
  return IP.replace(".", "[.]")

print(defang("255.100.50.0")) # "255[.]100[.]50[.]0"