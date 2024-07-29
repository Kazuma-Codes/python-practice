try:
    n = int(input("Enter any number, or press Enter to skip: "))
    for i in range(n, -1, -5):
        print(i)
except ValueError:
    for i in range(105, -7, -5):
        print(i)
