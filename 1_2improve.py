def countchar(s1,s2,s3):
    s1_count=0
    s2_count=0
    s3_count=0

    for i in range(len(s1)):
        if s1[i]==" ":
            s1_count=s1_count+0
        else:
            s1_count=s1_count+1

    for i in range(len(s2)):
        if s2[i]==" ":
            s2_count=s2_count+0
        else:
            s2_count=s2_count+1

    for i in range(len(s3)):
        if s3[i]==" ":
            s3_count=s3_count+0
        else:
            s3_count=s3_count+1

    maxx = s1_count

    if s1_count==s2_count==s3_count:
        print("All three have same character count. The count is",maxx)
        
    elif s2_count>maxx :
        maxx = s2_count
        if s3_count > maxx :
            maxx = s3_count
            print("String 3 is the longest. It has",s3_count,"characters")
        else:
            print("String 2 is the longest. It has",s2_count,"characters")

    elif s3_count>maxx:
        print("String 3 is the longest. It has",s3_count,"characters")

    else :
        print("String 1 is the longest. It has",s1_count,"characters")

s1 = input("Enter first string : ")
s2 = input("Enter second string : ")
s3 = input("Enter third string : ")

countchar(s1,s2,s3)
