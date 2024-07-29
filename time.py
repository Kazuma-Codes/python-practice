def calculate_time(speed,distance):
    return distance/speed

x = float(input("distance in meter "))
y = float(input("time in sec"))

time = calculate_time(x,y)
print(f"{time}")