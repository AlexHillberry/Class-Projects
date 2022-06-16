def main():
    # Welcome
    print("Welcome, and Thank You for using FiberOne Installations")
    # Enter Company_Name
    naming = True
    company_name = ""
    while naming:
        company_name = (input("Please enter your company name to begin \n"))
        if company_name.isalpha():
            print(company_name + ", Go ahead with your order")
            naming = False
        else:
            print("You must enter alpha-numeric characters only \n")
        # Enter Cable_Length
    shopping = True
    while shopping:
        cable_length = int(input("Please enter the amount of cable to be installed in feet \n"))
        if cable_length >= 100:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.7)
        if cable_length < 100:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.87)
        continue_purchase = input("Would you like to place another order Y/N \n")
        if continue_purchase == "N":
            shopping = False
    print("Thank you for using FiberOne Installations!")


# where the code starts
main()
