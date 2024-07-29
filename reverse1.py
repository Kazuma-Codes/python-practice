x = input("Enter any number, or press Enter to skip ")

if x:
    n = int(x)
    for i in range(n, -5, -7):
        print(i)
else:
    for i in range(105, -5, -7):
        print(i)
