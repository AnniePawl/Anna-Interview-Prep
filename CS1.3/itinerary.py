# Write a function to keep track of islands you have visited 




def get_itinerary(tickets):
  order = []
  # build dictionary 
  for item in tickets:
    from_island = item[0]
    to_island = item[1]

    from_to_dictionary[from_island] = to_island

  # find the start
  for from_island in from_to_dictionary.keys():
    if from_island not in  from_to_dictionary.values():
      break 

  print(start_island)
  return order


tickets = [("Noodle", "Jungalw"), ("Korok", "Bunpun"), ("Bunpun", "Noodle"), ("Jungalow", "Astra Nova")]

print(get_itinerary(tickets))
# [Korok, Bunpun, Noodle, Jungalow, Astra Nova]