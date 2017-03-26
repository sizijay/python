def investment(amount,rate,years):
    if amount <= 0:
        return 0
    else :
        if years >= 1:
            if years == 1:
                return amount+((amount*rate)/100)
            else:
                return investment(amount+((amount*rate)/100),rate,years-1)

amount = int(input("Enter the investment amount : "))
rate = int(input("Enter the interest rate : "))
years = int(input("Enter the number of years : "))
print(investment(amount,rate,years))
