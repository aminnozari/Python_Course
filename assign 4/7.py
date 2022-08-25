a=int(input("enter numberm : \n"))
b=int(input ("enter numbern : \n"))
bmm=1
for i in range (1,min(a,b)+1,1):
    if a%i==0 and b%i==0 :
        bmm=i

kmm=int(a/bmm*b)
print ("kmm : " , kmm )