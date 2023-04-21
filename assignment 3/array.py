import random
n=int(input ("please enter number of array chars:"))
i=1
number =[]
while (n>=i):
    rnum = random.randint(0,200)
    if rnum not in number:
        number.append(rnum)
        n=n-1
        
print(number)
    


    
