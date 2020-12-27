import random
import time
print("Welcome to Pydice, the dice rolling simulator! Roll any amount of classic dice or roll a custom dice, with the smallest and largest number of your choice.")
def RollingEffect():
    print("\n")
    print("Shaking dice")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("..")
    time.sleep(0.5)
    print(".")
    print("\n")

#Define roll dice
def RollDice(rolls):
    RollingEffect()
    while rolls != 0:
        dice_result = random.randint(1,6)
        print(dice_result)
        print("\n")
        rolls -= 1
    MainGame()

#Choose Option
def MainGame():
    print("1 - Roll a die")
    print("2 - Roll multiple dice")
    print("3 - Custom dice")
    print("4 - Exit")
    choice = input("Select one: ")
    while choice not in ["1","2","3","4"]:
        choice = input("Invalid choice. Please try again: ")

    #Run chosen option
    if choice == "1":
        RollDice(1)
    elif choice == "2":
        print("\n")
        dice_quantity = int(input("How many dice do you want to roll? "))
        RollDice(dice_quantity)

    elif choice == "3":
        print("\n")
        smallest_number = int(input("Smallest number: "))
        largest_number = int(input("Largest number: "))
        RollingEffect()
        custom_dice_result = random.randint(smallest_number,largest_number)
        print(custom_dice_result)
        print("\n")
        MainGame()
    else:
        exit()
MainGame()
