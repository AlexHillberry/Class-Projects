# This week we will work with loops. For this week’s assignment, write a program that uses a while loop to determine
# how long it takes for an investment to double at a given interest rate. The input will be an annualized interest
# rate and the initial investment amount and the output is the number of years it takes an investment to double.
# A=P(1+rt)

def banking():
    print("Welcome to the MarginLine Banking Investment Calculator.")
    principal = float(input("Please enter your initial investment amount: \n"))
    rate = float(input("Please enter the desired annual interest: \n"))
    time = 0
    while principal < (principal * 2):
        simple_interest = float(principal*(1+rate/100*time))
        time += 1
        if simple_interest == principal*2:
            print("Your investment doubles in", float(time), "years")
            continue_banking = input("Would you like to calculate a new investment? Type Y/N \n")
            while continue_banking.lower() not in ("y", "n"):
                continue_banking = input("You must type Y/N \n")
            if continue_banking.lower() == "y":
                banking()
            elif continue_banking.lower() == "n":
                break


if __name__ == '__main__':
    banking()
