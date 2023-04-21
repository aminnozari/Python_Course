array = []
n     = int(input('Enter number : '))
def khayyam(n):
    for i in range(n):
        array.append([1]*(i+1))
        
    for i in range(2,n):  
        for j in range(1,i)  :
            array[i][j]=array[i-1][j-1]+array[i-1][j]
            
    return(array)

khym = khayyam(n)
for i in range(n):
    print(*array[i])