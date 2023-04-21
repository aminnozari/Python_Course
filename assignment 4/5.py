import math
x=int(input("add ra vared konid: "))
for i in range(x):

    if math.factorial(i)==x:
        print("yes")
        exit()

print("no")