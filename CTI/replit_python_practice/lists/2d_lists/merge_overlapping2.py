# Given three intervals, merge overlapping intervals 
# Assume intervals are sorted
import merge_overlapping2

def merge_overlapping3(intervals):
  for i in range(len(intervals)):
    


# def merge_overlapping2(intervals):
#   x1 = intervals[0][0]
#   x2 = intervals[1][0]
#   y1 = intervals[0][1]
#   y2 = intervals[1][1]
  
#   result = []
#   if y1 >= x2:
#     result.append([x1,y2])
#   else:
#     return intervals
#   return result



print(merge_overlappying([[1,3],[2,6],[8,10]])) #[[1,6], [8,10]]
print(merge_overlappying([[1,3],[2,6],[5,10]])) #[[1,10]]