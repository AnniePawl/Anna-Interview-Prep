# Given two intervals, check if theya re overlapping - if so, return new, overlapping interval range 

def merge_overlapping(intervals):
  if intervals[0][1] > intervals[1][0]:
    return [[intervals[0][0],  intervals[1][1]]]
  else:
    return intervals
  
def merge_overlapping2(intervals):
  x1 = intervals[0][0]
  x2 = intervals[1][0]
  y1 = intervals[0][1]
  y2 = intervals[1][1]
  
  result = []
  if y1 >= x2:
    result.append([x1,y2])
  else:
    return intervals
  return result



print(merge_overlapping([[1,3],[2,6]])) # [[1,6]]
print(merge_overlapping([[1,3],[4,6]])) # [[1,3][4,6]]

print(merge_overlapping2([[1,3],[2,6]])) # [[1,6]]
print(merge_overlapping2([[1,3],[4,6]])) # [[1,3][4,6]]