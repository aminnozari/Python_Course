array=[]
data=[]
n=int(input("enter size of your array:"))
while n>0:
   narray=int(input("please enter a number of array:"))
   array.append(narray)
   data.append(narray)
   n-=1

if sorted(array)==data:
    print(sorted(array))
    print("yes array is sorted")
else:
    print(data)
    print("no the array is not sorted")