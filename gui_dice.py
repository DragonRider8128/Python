from guizero import *
from random import randint
import time

#Make app window
app = App(title="Dice roller",height=600,width=1000)
app.bg = (175,238,238)
#Create welcome text
welcome = Text(app,text="Welcome to dice roller!")
welcome.text_size = 50
welcome.text_color = "orange"
welcome.font = "impact"

#Text boxes for lowest and highest values for die
lowest_number= TextBox(app,text="Enter lowest value here")
highest_number = TextBox(app,text="Enter highest value here")
lowest_number.width = 21
lowest_number.text_size = 15
highest_number.width = 21
highest_number.text_size = 15

#Dice image
image = Picture(app,image ="dice.png")

#Roll dice function for button
def roll_dice():
    number_text.clear()
    try:
        number = str(randint(int(lowest_number.value),int(highest_number.value)))
        number_text.value = number
    except:
        app.error("Error","Values are not whole numbers or first value is higher than the second.")

#Roll dice button
roll = PushButton(app,roll_dice,text = "Click me to roll a die!")
roll.text_size = 15
roll.text_color = "blue"
roll.font = "Verdana"

#Create text to display number
number_text = Text(app,text="")
number_text.text_size = 100
number_text.text_color = "red"

app.display()
