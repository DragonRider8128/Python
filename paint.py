from guizero import *

app = App(title="Macrohard Draw",width=1000,height=600)
print("hello world")
app.bg = "white"
app.font = "Arial"
app.text_size = 13

def change_bg():
    app.bg = bg.value
    
colour = Combo(app,options=["black","white","red","green","blue","orange","turquoise","light green","cyan","yellow"])
bg = Combo(app,command=change_bg,options=["white","black","red","green","blue","orange","turquoise","light green","cyan","yellow"])
tool = Combo(app,options=["line","rectangle","oval"])
width = Slider(app,start=1,end=10)
painting = Drawing(app,height="fill",width="fill")
clear = PushButton(app,command=painting.clear,text="Clear")

def start(event):
    painting.last_event = event
    painting.first_event = event
    painting.last_shape = None
def draw(event):
    if tool.value == "line":
        painting.line(painting.last_event.x,painting.last_event.y,event.x,event.y,color=colour.value,width=width.value)
        painting.last_event = event

    if tool.value == "rectangle":
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        rectangle = painting.rectangle(painting.first_event.x,painting.first_event.y,event.x,event.y,color=colour.value)
        painting.last_shape = rectangle

    if tool.value == "oval":
        if painting.last_shape is not None:
            painting.delete(painting.last_shape)
        oval = painting.oval(painting.first_event.x,painting.first_event.y,event.x,event.y,color=colour.value)
        painting.last_shape = oval

painting.when_mouse_dragged = draw
painting.when_left_button_pressed = start

app.display()
