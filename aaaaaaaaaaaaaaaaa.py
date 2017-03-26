def factorial(n):
    num=1
    while n>=1:
        num=num*n
        n=n-1
    return num
#for i in range(1,x):
x=int(input("enter number :"))
print(factorial(x))
