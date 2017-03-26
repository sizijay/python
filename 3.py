def fibonacci(n):
    fib= 0
    first = 0
    second = 1
    if (n<1):
        return ("Invalid Input...!")
    elif (n<=2):
        return (1)
    else:
        for i in range(1,n):
            fib = first + second
            first = second
            second = fib  

    return(fib)
print(fibonacci(12))
