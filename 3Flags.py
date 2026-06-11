import turtle
import random

window=turtle.Screen()
window.bgcolor("white")
turtle.title("Flag Guesser")

bob= turtle.Turtle()
bob.shape("turtle")
bob.pensize(50)
bob.color("black")
bob.fillcolor("black")

points = 0
life = 3

def Germany():

    bob.pendown()
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()
    bob.penup()

    bob.goto(-100,-100)
    bob.fillcolor("red")
    bob.pencolor("black")
    bob.pendown()
    bob.begin_fill()
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()

    bob.penup()
    bob.fillcolor("yellow")
    bob.pencolor("black")
    bob.begin_fill()
    bob.pendown()
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.end_fill()

    bob.penup()

def Bangladesh():
    bob.pendown()
    bob.fillcolor("dark green")
    bob.pencolor("black")
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(300)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(200)
    bob.end_fill()
    bob.penup()

    bob.goto(-30,60)
    bob.fillcolor("red")
    bob.begin_fill()
    bob.pendown()
    bob.circle(50)
    bob.end_fill()

def Netherlands():
    bob.pendown()
    bob.fillcolor("red")
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()
    bob.penup()

    bob.goto(-100, -100)
    bob.fillcolor("white")
    bob.pencolor("black")
    bob.pendown()
    bob.begin_fill()
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.end_fill()

    bob.penup()
    bob.fillcolor("blue")
    bob.pencolor("black")
    bob.begin_fill()
    bob.pendown()
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.end_fill()

def Japan():
    bob.pendown()
    bob.fillcolor ("white")
    bob.pencolor("black")
    bob.begin_fill()
    bob.forward(100)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(300)
    bob.left(90)
    bob.forward(200)
    bob.left(90)
    bob.forward(200)
    bob.end_fill()
    bob.penup()

    bob.goto(-30,60)
    bob.fillcolor("red")
    bob.begin_fill()
    bob.pendown()
    bob.circle(50)
    bob.end_fill()

flags= [Germany,Bangladesh,Netherlands,Japan]

while life>0 and len(flags)>0:
    bob.reset()
    flag = random.choice(flags)
    flag()
    answer = input("Guess the flag ")

    if answer == flag.__name__:
        print("Correct Answer!")
        points = points + 1
        print("Points: ",points)
        print("Life: ",life)
        flags.remove(flag)
    else:
        print("Wrong answer,try again later")
        life = life - 1
        print("Points:  ",points)
        print("Lives:  ",life)
print("Game over!")

#Germany()
#Bangladesh()
#Netherlands()
#Japan()

turtle.done()



