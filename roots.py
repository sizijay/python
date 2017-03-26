def roots(a,b,c):
    delta=((b**2)-(4*a*c))
    if (delta<0):
        print("\nThe roots are complex...\n")
    elif (delta==0):
        print("\nRoots are real and equal....\n")
    else:
        print("\nRoots are real...\n")
    print("Roots =   "+str(((-b)+(delta**(1/2)))/(2*a))+"     &     "+str(((-b)-(delta**(1/2)))/(2*a))+"\n\n\t\t***********************\n")
w=1
while (w==1):
    eq=input("\nEnter the equation in the format => ax2+bx+c=0  to find the roots\nNote-:range (a,b,c)=[0,9]\n\t")
    if ((len(eq)<10) or (len(eq)>10)):
        print("\nPlease enter the equation in the correct format..\n")
        continue
    a=int(eq[0])
    b=int(eq[4])
    c=int(eq[7])

    roots(a,b,c)
    w=2
