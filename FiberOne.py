def main():
    # Welcome
    print("==========================================================")
    print("Welcome! Thank You for using FiberOne Installations.")
    print("==========================================================")
    # Enter Company_Name
    naming = True
    company_name = ""
    while naming:
        company_name = (input("Please enter your company name to begin \n"))
        if company_name.isalnum():
            print(company_name + ", Go ahead with your order!")
            naming = False
        else:
            print("You must enter alpha-numeric characters only \n")
        # Enter Cable_Length
    shopping = True
    while shopping:
        cable_length = int(input("Please enter the amount of cable to be installed in feet \n"))
        if cable_length <= 100:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.87)
        elif 100 < cable_length <= 250:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.8)
        elif 250 < cable_length <= 500:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.7)
        elif cable_length > 500:
            print("Thank you", company_name, ",Your total expense is $", cable_length * 0.5)
        continue_purchase = input("Would you like to place another order Y/N \n")
        while continue_purchase.lower() not in ("y", "n"):
            continue_purchase = input("You must type Y/N \n")
        if continue_purchase.lower() == "n":
            break
    print("==========================================================")
    print("Thank you for using FiberOne Installations! ☺")
    print("==========================================================")


# where the code starts
main()
