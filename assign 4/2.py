import math

a=int(input("enter the coefficient of x^2: "))

b=int(input("enter the coefficient of x: "))

c=int(input("enter the third coefficient:"))

delta=b**2-4*a*c

if delta==0 :

    x=(-b + math.sqrt(delta))

    print("Moadele Yek javab darad. X=",x)

elif delta<0:

    print("Moadele javabe haghighi nadarad!")

else :    

    x1=(-b + math.sqrt(delta))/(2*a)

    x2=(-b - math.sqrt(delta))/(2*a)

    print("Moadele 2 javab darad.\n X1= ",x1, "\nX2= " , x2)

