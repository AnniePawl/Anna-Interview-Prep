# Given list of countries cities in it , then a list of cities:
# Print which country each city is located in 
major_cities = {}
for i in range(int(input())):
  locations = input().split()
  major_cities[locations[0]] = locations[1:]
print(major_cities)

target_cities = []
for i in range(int(input())):
  target_cities.append(input())

i = 0
for key, value in major_cities.item():
  if target_cities[i] == value:
    i + 1
    return key
  else:
    break


