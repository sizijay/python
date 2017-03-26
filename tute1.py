m=0
mu =1

for n in range (1,10):
    x =1
    while x<10.0:
        x = x + 0.1 
        while m > n*x:
            m=x**mu
            print(mu)
            if m==x*n:
                print("n = ",n)
                print("x = ",x)
            mu = mu + 1
        mu = 1
            
