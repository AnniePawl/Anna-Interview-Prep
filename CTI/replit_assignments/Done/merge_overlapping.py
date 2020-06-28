# Given collection of intervals, merage all overlapping intervals 

def merge_overlapping(intervals):
  if intervals = []:
    return []
  else:
    new_intervals = [intervals[0]]
    for i in range(1, len(intervals)):
      if new_intervals[-1][1] >= intervals[i][0]:
        new_intervals[-1] = [new_intervals[-1][0], intervals[i][1]]
      else:
        new_intervals.append(intervals[i])
    return new_intervals
  

print(merge_overlapping([[2,6],[1,3],[8,10],[15,18]]))
# [1,6],[8,10],[15,18]https://www.loom.com/share/51fbc39926f641da874046f7fef99fe9