# This week we will work with loops. For this week’s assignment, write a program that uses a while loop to determine
# how long it takes for an investment to double at a given interest rate. The input will be an annualized interest
# rate and the initial investment amount and the output is the number of years it takes an investment to double.
# currency = "${:,.2f}". format(amount)
# A=P(1+rt)

def banking():
    print("Welcome to the MarginLine Banking Investment Calculator.")
    principal = int(input("Please enter your initial investment amount: \n"))
    rate = float(input("Please enter the desired annual interest: \n"))
    time = 0
    while principal < (principal * 2):
        simple_interest = float(principal*(1+rate/100*time))
        time += 1
        if simple_interest == principal*2:
            print("Your investment doubles at year", time)
            print("Would you like to try again?")


if __name__ == '__main__':
    banking()
