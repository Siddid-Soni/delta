n = int(input("enter the size of the grid: "))

for i in range(0, n*2-1):
    if i%2==0:
        for j in range(0,n-1):
            print("  |", end="")
    else:
        for k in range(0,n):
            print("--", end=" ")

    print()