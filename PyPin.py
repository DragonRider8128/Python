
import random
import time
#Welcome
generate = input("Welcome to PyPin!\nEver wanted to protect your accounts with secure passwords but couldn't make and easy to remember ones? Well just run PyPin to get a secure but easy to remember password within seconds!\nDo you want to generate a password? y/n ")

while generate.upper() != "Y" and generate.upper() != "N":
    generate = input("Invalid answer, please try again. ")
repeat = True

while repeat == True:
    #Put together password
    if generate.upper() == "Y":
        #Lists of components in password
        nouns = ["pizza","tiger","lion","toilet","computer","tablet","smartphone","flag","sack","sugar","course","wire","python"]

        adjectives = ["lush","green","silly","furious","rapid","giant","tiny","micro","tasty","loud","quiet","thirsty","bulky","easy","intermediate","difficult","long","vast","short"]

        numbers = [0,1,2,3,4,5,6,7,8,9]

        special_characters = ["£","$","@","#","%","*"]
        #Generate password
        random.shuffle(nouns)
        random.shuffle(adjectives)
        random.shuffle(numbers)
        random.shuffle(special_characters)

        #Reveal password
        print("Generating password...")
        time.sleep(1)
        print(str(numbers[0]) + str(numbers[1]) + str(numbers[2]) + str(special_characters[0]) + adjectives[0] + nouns[0] + str(special_characters[1]) + str(special_characters[2]))

        run_again = input("Do you want to generate a new password? y/n ")

        while run_again.upper() != "Y" and run_again.upper() != "N":
            run_again = input("Invalid answer, please try again. ")

        if run_again.upper() == "N":
            repeat = False

    else:
        print("Sad to see you go. Bye!")
        repeat = False
        exit()

print("I hope you enjoyed! Bye!")
