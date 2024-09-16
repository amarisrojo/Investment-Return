#Investment Return
'''
script: InvestmentReturn
action: calculates rate of return for given principle, return, yes
author: Amaris Rojo
date: 08/29/2024
'''
#declare variables
startingInvestment = 1000
returnRate = .07

# deposit after 10, 20, 30 years
yrs10 = 0.00
yrs20 = 0.00
yrs30 = 0.00

#calculate returns using a= p(1+r)^n ( n = 10,20,30)
#run formula
yrs10 = startingInvestment * (1 + returnRate)**10
yrs20 = startingInvestment * (1 + returnRate)**20
yrs30 = startingInvestment * (1 + returnRate)**30

#Create output message
#amount at nth years
print("You're total amount of savings after 10 years is $",yrs10)
print("You're total amount of savings after 20 years is $", yrs20)
print("You're total amount of savings after 30 years is $",yrs30)
