def calculate_speed(distance, time, distance_unit, time_unit):
    if distance_unit == "km":
        distance *= 1000
    if time_unit == "hr":
        time *= 3600
    elif time_unit == "min":
        time *= 60
    return distance / time

distance_unit = input("distance in m or km ").lower()
time_unit = input("time in min or hr").lower()

x = float(input(f"enter distance in({distance_unit} )"))
y = float(input(f"enter time in ({time_unit})"))

speed = calculate_speed(x,y,distance_unit,time_unit)

if distance_unit == "km"  and time_unit == "hr":
    print(f"sped in km per hr is {speed}")
elif distance_unit == "m" and time_unit == "min":
    print(f"speed in m per min is {speed} ")
else:
    print(f"speed of the object is {speed}")