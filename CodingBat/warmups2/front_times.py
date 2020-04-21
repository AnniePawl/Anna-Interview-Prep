# Given a string of non-negative int n, front = first 3 characters. Return n copies of front


def front_times(str, n):
    front = str[:3]
    return front * n


def front_times_v2(str, n):
    result = ""
    front = str[:3]
    for i in range(n):
        result += front
    return result


print(front_times("Gluegun", 3))  # GluGluGlu
print(front_times("Cinnabun", 2))  # CinCin
print(front_times("Berry", 1))  # Ber

print(front_times_v2("Puppy", 4))  # PupPupPup
