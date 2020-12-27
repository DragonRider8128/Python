#Currencies
#£1.00 = €1.11
#£1.00 = $1.29
#€1.00 = £0.90
#$1.00 = £0.78

#Welcome
print("Welcome to Currency Converter! Select an option and enter the amount of money you want to convert. ")

#Conversion function
def convert(conversion_amount,result_currency):
    conversion = round(conversion_amount*result_currency,2)

    if result_currency == 1.11:
        print("€" + str(conversion) + "\n")
    if result_currency == 1.29:
        print("$" + str(conversion) + "\n")
    if result_currency == 0.90 or result_currency == 0.78:
        print("£" + str(conversion) + "\n")

    menu()

#Menu function
def menu():
    #Display options
    print("1 - Pounds - Euros")
    print("2 - Euros - Pounds")
    print("3 - Pounds - US Dollars")
    print("4 - US Dollars - Pounds")
    print("5 - Exit")

    #Ask for choice and check if it's valid
    choice = input("\nSelect an option: ")
    while choice not in ["1","2","3","4","5"]:
        choice = input("Invalid input. Please try again: ")

    #Convert currency based on user input
    if choice == "1":
        pounds = float(input("Enter amount in Pounds: £"))
        while type(pounds) == "str":
            pounds = input("Invalid input. Please try again: ")
        convert(pounds,1.11)

    elif choice == "2":
        euros = float(input("Enter amount in Euros: €"))
        while type(euros) == "str":
            euros = input("Invalid input. Please try again: ")
        convert(euros,0.90)

    elif choice == "3":
        pounds = float(input("Enter amount in Pounds: £"))
        while type(pounds) == "str":
            pounds = input("Invalid input. Please try again: ")
        convert(pounds,1.29)

    elif choice == "4":
        dollars = float(input("Enter amount in Dollars: $"))
        while type(dollars) == "str":
            dollars = input("Invalid input. Please try again: ")
        convert(dollars,0.78)

    else:
        print("Sad to see you go. :(")
        exit()
menu()
