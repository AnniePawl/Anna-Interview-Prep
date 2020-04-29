# Squirrels spend most of day palying. They play when temp is between 60 and  90 inclusive. Unless its summer, then upper limit is 100. Given an int temp and a  boolean, return True if squirrels play. 

def squirrel_play(temp, is_summer):
  return temp in range(60,101 if is_summer else 91)
  


print(squirrel_play(70, False)) #True
print(squirrel_play(95, False)) #True
print(squirrel_play(95, True)) #True