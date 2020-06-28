# Given three intervals, merge overlapping intervals 
# Assume intervals are sorted

def merge_overlapping2(intervals):
  new_intervals = [intervals[0]]
  for i in range(1, len(intervals)):
    if new_intervals[-1][1] >= intervals[i][0]:
      new_intervals[-1] = [new_intervals[-1][0], intervals[i][1]]
    else:
      new_intervals.append(intervals[i])
  return new_intervals
 
  
  

print(merge_overlapping2([[1,3],[2,6],[8,10]])) #[[1,6], [8,10]]
print(merge_overlapping2([[1,3],[2,6],[5,10]])) #[[1,10]
print(merge_overlapping2([[1,3],[2,6],[5,10],[7,15],[20,21]])) #[[1,15],[20,21]]