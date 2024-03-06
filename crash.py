from turtle import * 
from random import randint, choice

############# DEFINE CLASSES AND FUNCTIONS #############
def road():
    r = Turtle()
    r.hideturtle()
    r.speed(0)
    r.goto(-160,500)
    r.fillcolor("gray")
    r.begin_fill()
    r.goto(160,500)
    r.goto(160,-500)
    r.goto(-160,-500)
    r.end_fill()

class Car(Turtle):
    '''
    Constructor
    '''

    '''
    drive() Method
    '''

    '''
    relocate() Method
    '''



############# YOUR PROGRAM  #############
screen = Screen()
screen.tracer(0)
screen.bgcolor("green")
road()
screen.register_shape("one.gif")
screen.register_shape("two.gif")
screen.register_shape("three.gif")
screen.register_shape("four.gif")
screen.register_shape("five.gif")
screen.tracer(1)

images = ["one.gif", "two.gif", "three.gif", "four.gif", "five.gif"]






screen.mainloop()