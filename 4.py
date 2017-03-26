def power(base,expo):
    if expo >= 0:
        if expo == 0:
            return 1
        elif expo == 1:
            return base
        else:
            return base * power(base,(expo-1))

    else:
        if expo == 0:
            return 1
        else:
            return (1/base) * power(base,(expo+1))

base = int(input("Input value for base : "))
expo = int(input("Input value for exponent : "))

print(power(base,expo))
    
