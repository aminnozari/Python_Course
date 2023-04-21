Input = int(input("Enter Number"))
fib = []
fib.append(1)
fib.append(1)
for i in range(2, 7):
    fib.append(fib[i-2]+fib[i-1])
print(Input,"Number Of Fibonacci ", fib)