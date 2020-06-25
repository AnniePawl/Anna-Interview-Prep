# Given collection of intervals, merage all overlapping intervals 

def merge_overlapping(intervals):
  for i in range(len(intervals)-1):
    if intervals[i+1][0] < intervals[i][1]:
      intervals[i][0], intervals[i][1] = intervals

print(merge_overlapping([[2,6],[1,3],[8,10],[15,18]]))
# [1,6],[8,10],[15,18]