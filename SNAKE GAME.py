import turtle
import math
import random


wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("Snake Game")

snake = turtle.Turtle()
snake.color("blue")
snake.shape("square")
snake.penup()
snake.shapesize(stretch_wid=0.6, stretch_len=1.6)
snake.speed(0)


outline = turtle.Turtle()
outline.penup()
outline.setposition( -300,-300 )
outline.pensize( 3)
outline.pendown()
outline.speed( 6)
outline.color("black")
outline.pencolor( "black" )

for size in range( 4 ):
    outline.forward( 600)
    outline.left( 90 )
outline.hideturtle()


food = turtle.Turtle()
food.color("orange")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(-100, 100)

speed = 1

def turnleft():
    snake.left(90)

def turnright():
    snake.right(90)


turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")

while True:
    
    snake.forward(speed)
    d = math.sqrt(pow(snake.xcor()-food.xcor(), 2) + pow(snake.ycor()-food.ycor(), 2))
    
    if d < 20:
       food.setposition(random.randint(-300, 300), random.randint(-300, 300))
       speed+=1

    if snake.xcor()>280 or snake.xcor()<-280 or snake.ycor()>280 or snake.ycor()<-280:
        snake.hideturtle()
        food.hideturtle()
        outline.penup()
        outline.setposition(-100,0)
        outline.write("GAME OVER", align = 'left' , font = ("Arial",24,"bold"))
    

