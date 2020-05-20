# Return True if dish starts and ends w/ same letters as animals name
def feast(animal, dish):
  return animal[0] == dish[0] and animal[-1] == dish[-1]

print(feast("brown bear", "bear claw")) # False 
print(feast("chickadee", "chocolate cake")) # True
print(feast("great blue heron", "garlic naan")) # True 