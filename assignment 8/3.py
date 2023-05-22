n = int(input("Enter the size of the rhombus: "))
for i in range(n):
    print(" " * (n-i-1) + "*" * (i+1) + "*" * i)
for i in range(n-2, -1, -1):
    print(" " * (n-i-1) + "*" * (i+1) + "*" * i)