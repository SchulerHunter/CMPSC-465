def fibonacci(n): 
    if n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 

FibArray = [0,1]
with open(input("Provide file path: "), "r") as f:
    print(fibonacci(int(f.readline())))