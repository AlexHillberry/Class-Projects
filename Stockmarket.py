def stockmarket():
    # dictionary of stocks
    stocks = {
        "WMT": 129.09, "GOOGL": 2235.77, "AAPL": 150.17, "AMZN": 113.54, "CVS": 95.37,
        "WBA": 38.02, "MRNA": 166.97, "PFE": 51.74, "MCK": 329.88, "ABC": 142.19, "LLY": 331.48
    }

    print("Welcome to the Pythonic Stock Exchange!")
    # seperator and print statement for available choices
    separator = " "
    print("The current daily traded stocks are: \n", separator.join(stocks))
    # while loop for input anc error msg
    while True:
        ticker = input("Please type a stock name to see current traded value \n")
        if ticker in stocks:
            print("The current traded price for", ticker, "is", stocks[ticker])
            break
        else:
            print("Please enter a valid stock from the list provided.")


if __name__ == '__main__':
    stockmarket()
