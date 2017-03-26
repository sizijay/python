def factorial(n):
    if n>=0:
        if n==0:
            return 1
        else:
            return n*factorial(n-1)

    else:
        return ("Invalid input")

num = int(input("Enter a number to get n'th factorial : "))
print(factorial(num))
