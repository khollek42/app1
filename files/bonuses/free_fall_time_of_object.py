def calculate_time(h, g=32.174049586):
    t = (2 * h / g) ** 0.5
    return t

distance = float(input("How many feet is the fall? "))
time = calculate_time(distance)

print(time)