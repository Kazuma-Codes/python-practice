x = float(input("distance "))


y = float(input("time "))
def to_calculate_speed(distance,time):
    return distance / time


speed = to_calculate_speed(x, y)
print(f"{speed}")

#The f before the string indicates that this is an f-string,
#  which allows us to embed expressions inside curly braces {}.i.e speed