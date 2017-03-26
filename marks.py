while True:
    a=input("enter your name")
    b=input("enter the first test grade")
    c=input("enter the second test grade")
    d=input("enter the third test grade")
    e=(int(b)+int(c)+int(d))/3
    print(a)
    print(e)
    if e>=60:
        print("pass")
        if e<=70:
            print("marginal")
    else:
        print("fail")
