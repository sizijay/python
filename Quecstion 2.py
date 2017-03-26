x = float(input("please enter grades/marks: "))
y = float(input("please enter grades/marks: "))
z = float(input("please enter grades/marks: "))
average = (x+y+z)/3
print(average)
if average >= 60:
    print("You passe")
    if average < 70:
        print("You are in marginal")
else:
    print("You failed")
