def encript(line,key):
    l=[]
    for i in range (len(line)):
        l.append(chr(ord(line[i])+key))
    print(''.join(l))
    return(''.join(l))
x=str(input("enter your massege="))
y=int(input("enter key number="))
p=encript(x,y)
def decrypt(p,key):
    l=[]
    for i in range (len(p)):
        l.append(chr(ord(p[i])-key))
    print (''.join(l))    
decrypt(p,y)        




        
        

