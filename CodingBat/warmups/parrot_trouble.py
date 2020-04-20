# We have a loud parrot. Hour parameter is current hour in range 0...23. We are in trouble if  parrot is talking and hour is before 7 or after 20. Return True if we are in trouble


def parrot_trouble(talking, hour):
    return(talking and (hour < 7 or hour > 20))


print(parrot_trouble(True, 6))  # True
print(parrot_trouble(True, 7))  # False
print(parrot_trouble(False, 6))  # False
