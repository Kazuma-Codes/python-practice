#Do not print banana:
x = ["apple","banana","orange"]
for y in (x):
    if y == ("banana"):
        continue
    print(y)
    #skips banana and prints the remaining items