import random
print("Welcome to PyGuess! Here's how it works:\nThe computer will guess a random number from 1 to 100.\nYou have to try and guess that number.\nYou will be prompted if your guess is too low or too high.\n")
start = input("Do you want to begin? y/n ")
while start.upper() != "Y" and start.upper() != "N":
    start = input("Please enter a valid answer: ")

number = random.randint(1,100)
if start.upper() == "Y":
    guessed = False
    attempts = 0
    number = random.randint(1,100)
    guess = input("\nGuess a number: ")

    while guessed == False:
        if int(guess) < number:
                print("Guess is too LOW!")
                attempts += 1
                print("\n")
                guess = input("Try again: ")
        elif int(guess) > number:
            print("Guess is too HIGH!")
            attempts += 1
            print("\n")
            guess = input("Try again: ")
        else:
            print("\n")
            print("Well Done! You guessed the number!")
            print("It took you " + str(attempts) + " attempts.")
            guessed = True
else:
    print("Sad to see you go. Bye!")
