
print("interest calculator")
startAmount = input("type starting amount: ")
interestRate = input("type interest rate (ex 6% = 0.06): ")
years = input("type the number of years to calculate the interest: ")


def calcInterest(starting = 0, rate = 0, years = 0):
    yearCount = 0
    print("\n" + str(starting) + "$ is the start amount\n" + str(rate) + " is the rate of interest\n" + str(years) + " is how many years of interest you'll get")

    while yearCount != int(years):
        global startAmount
        yearCount += 1
        answer = float(startAmount) * float(rate) + float(startAmount)
        startAmount = float(answer)
    
    print("your answer is " + str(round(answer, 2)))

calcInterest(startAmount, interestRate, years)