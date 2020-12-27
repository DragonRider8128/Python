#Intro
print("Welcome the Don't Die, the epic RPG action game in which there is only one rule. Do not die! Go through the story making careful desicions but remember one choice can mean life or death. Figuratively and literally.")

#Begin
start = input("Do you wish to proceed on your adventure? y/n ")
while start.upper() not in ["Y","N","YES","NO"]:
    start = input("Invalid input. Please try again. ")

#Play game or exit the game
if start.upper() in ["Y","YES"]:
    lost = input("\nYou are walking home late at night from work. You have been walking for over an hour but still haven't arrived home. You are tired, thirsty and hungry. You come to a dead end and find an abandoned cabin, which looks old and wrecked but habitable. Do you sleep overnight in the cabin and find your way home in the morning or continue through a nearby wood and find home now? Sleep or wood? " )
    while lost.upper() not in ["SLEEP","WOOD"]:
        lost = input("That is not an option. Try again. ")
    if lost.upper() == "SLEEP":
        bandages = input("\nIt is now 7pm in the morning and as you wake up you fall into a pile of sharp nails. You get a cut on your arm and it stings and hurts badly. You look around for bandages or plasters and find a dusty first aid kit. You open it and inside you find some dirty bandages. You can either use the old bandages or cover the cut with your shirt sleeve and hope for the best. What do you do? Bandages or ignore? ")
        while bandages.upper() not in ["BANDAGES","IGNORE"]:
            bandages = input("That is not and option. Try again. ")
        if bandages.upper() == "IGNORE":
            water = input("\nYou exit the cabin, holding you aching arm, and continue the way you came from, trying to find home. You are very thirsty. As you look around, you find a small pond filled with water, but no life. You examine it closely. Do you drink it to quench your thirst or hold on as you don't know how clean the water is. Drink or continue? ")
            while water.upper() not in ["DRINK","CONTINUE"]:
                water = input("This not an option. Try again. ")
            if water.upper() == "DRINK":
                print("T\nhe water tastes disghusting and it turns out that it is infected and contained a lethal virus calle YOU_DIEITIS. YOU DIED.")
            elif water.upper() == "CONTINUE":
                map = input("\nAs you continue to try and find your house, you find what seems to be an old warehouse. It's completely run down and isn't being used anymore. You have no option and you go inside. Inside, there are several computer screens and TVs. You find one displaying a map. As the warehouse is so old, the maps could be outdated, inaccurate and might lead you in the wrong direction. Do you use the maps or find your own way home? Map or own? ")
                while map.upper() not in ["MAP","OWN"]:
                    map = input("This is not an option. Try again. ")
                if map.upper() == "MAP":
                    print("\nYou follow the map and eventually find the street you live on - YOUAREADUMMY AVENUE. You find your house at the far end but becuase you were away for so long, it has become run down. But it is still habitable. YAY! YOU SURVIVED!")
                elif map.upper() == "OWN":
                    print("\nYou try to find your way home but never find it. Eventually your beard grows to long and you trip over it and break your skull. YOU DIED!")
        elif bandages.upper() == "BANDAGES":
            print("\nAs you walk outside, your cut stings. You continue walking. The pain in your arm becomes worse. Soon you notice the cut is infected as the bandages you used were too dirty and were full of germs. You find no medical attention.\nYOU DIED!")

    if lost.upper() == "WOOD":
        wolves = input("\nYou turn on a torch you have in your bag and continue down a muddy path. Suddenly, you hear howls. A pack of wolves is running towards you. Do you run out of the wood or turn and take a diversion? Back or diversion? ")
        while wolves.upper() not in ["DIVERSION","BACK"]:
            wolves = input("This is not an option. Try again. ")
        if wolves.upper() == "BACK":
            print("\nYou trip over a log and the wolves catch up with you. They eat you at a wolf party. YOU DIED!")
        elif wolves.upper() == "DIVERSION":
            map = input("\nIt turned out that the path you followewd led you out of the forest. As you continue to try and find your house, you find what seems to be an old warehouse. It's completely run down and isn't being used anymore. You have no option and you go inside. Inside, there are several computer screens and TVs. You find one displaying a map. As the warehouse is so old, the maps could be outdated, inaccurate and might lead you in the wrong direction. Do you use the maps or find your own way home? Map or own? ")
            while map.upper() not in ["MAP","OWN"]:
                map = input("\nThis is not an option. Try again. ")
            if map.upper() == "MAP":
                print("\nYou follow the map and eventually find the street you live on - YOUAREADUMMY AVENUE. You find your house at the far end but becuase you were away for so long, it has become run down. But it is still habitable. YAY! YOU SURVIVED!")
            elif map.upper() == "OWN":
                print("\nYou try to find your way home but never find it. Eventually your beard grows to long and you trip over it and break your skull. YOU DIED!")
else:
    print("Okay. You're one of those wimps who doesn't take risks. GO AWAY!")
