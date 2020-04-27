# Given an array of values you need to map the values on to a grid. Return an array of objects containing the original value, and a row and col that would represent the position of where the object would map on the grid. Assume the length of the original array is always a square e.g. 4, 9, 16 etc. Assume the grid has an equal height and width.

array = [1, 2, 3, 4]

def grid(array):
    length = len(array)  # length = 4 items
    width = int(length ** .5)
    bigArray = []
    for i in range(0, length, width):
        subarray = array[i:i+width]
        bigArray.append(subarray)
    return bigArray

  # returns 2dArray --> [[1, 2], [3, 4]]


def location(bigArray):  # take in value from array
    print(bigArray)
    location_dict = {}  # create dictionary to hold value + location
    # key = value from array (n), value = location(x,x)
    # for i, item in enumerate(bigArray)
    # Loop over every value the bigArray
    # Return the {value, (location)}


print(grid(array))
print(location(bigArray))
