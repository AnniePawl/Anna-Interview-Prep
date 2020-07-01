# Given number of records followed by name of candidate and number of votes in some state, count results and rturn number of votes for each candidate 
# Print canidates in alphabetical order 

records = {}
for i in range(int(input())):
  candidate, votes = input().split()
  # Account for same keys 
  if candidate in records:
    records[candidate] += int(votes) # make sure int 
  else:
    records[candidate] = int(votes)

for key, value in sorted(records.items()):
  print(key, value)


# Sample Input 
# 5
# McCain 10
# McCain 5
# Obama 9
# Obama 8
# McCain 1

# Sample Output 
# McCain 16
# Obama 17



