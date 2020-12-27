from faker import Faker
fake = Faker()

def GenerateDetails(repeat):
    while repeat != 0:
        print(fake.name())
        print(fake.email())
        print(fake.url())
        print(fake.phone_number())
        print(fake.address())
        print(fake.country())
        print(fake.longitude(),fake.latitude())
        print("\n")
        repeat = int(repeat) - 1
    Menu()

def Menu():
    print("Welcome to PyFake! Do you want to generate fake details? If you do, just run PyFake and get fake details in seconds!")
    print("1 - Generate fake details")
    print("2 - Generate multiple sets of fake details")
    print("3 - Exit")
    choice = input("Enter your choice: ")

    while choice not in ["1","2","3"]:
        choice = input("Invalid option. Please enter a new choice: ")

    if choice == "1":
        print("\n")
        GenerateDetails(1)
    elif choice == "2":
        quantity = input("How many sets of fake details do you want to generate?  ")
        print("\n")
        GenerateDetails(quantity)
    else:
        print("\n")
        print("Sad to see you go. Bye! :(")
        exit()
Menu()
