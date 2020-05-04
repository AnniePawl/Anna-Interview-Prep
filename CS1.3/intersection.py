# Write function that uses has table (dictionary) to find intersection between two unsorted arrays (lists) and return elements they have ic common as a list. 

def intersection(list1, list2):
  item_dictionary = {} # create empty dictionary
  intersection = [] # list to hold intersection numbers

  for item in list1:  # loop thru frst list 
    if item not in item_dictionary.keys(): # add to dict if not there already
      item_dictionary[item] = 1
    else:
      item_dictionary[item] +=1

  for item in list2: # loop thru second list
    if item in item_dictionary.keys(): # check if item already in dict
      item_dictionary[item] += 1 # if there, up count by 1

  for items in item_dictionary.items(): 
    if items[1] > 1: # if an item has more than one count, it means it appears in both numbers list
      intersection.append(items[0]) # add these intersection nums to our empty intersection array
  
  return intersection

  
print(intersection([3,4,5,6], [5,6,7,8])) # => [5,6]


