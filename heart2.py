import turtle
import time

# Set up the window
screen = turtle.Screen()
screen.bgcolor("white")

# Create turtle for heart
heart = turtle.Turtle()
heart.pensize(3)
heart.speed(0)
heart.fillcolor("red")

# Create turtle for text
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.goto(0, -240)
text.write("Made by Lexin", align="center", font=("Arial", 18, "bold"))

# Function to draw a heart of given size
def draw_heart(size):
    heart.clear()
    heart.penup()
    heart.goto(0, -size)
    heart.pendown()
    heart.begin_fill()
    heart.left(140)
    heart.forward(size)
    heart.circle(-size / 2, 200)
    heart.left(120)
    heart.circle(-size / 2, 200)
    heart.forward(size)
    heart.end_fill()
    heart.setheading(0)  # Reset angle

# Animate the heart beating
for _ in range(5):  # Number of beats
    draw_heart(180)
    time.sleep(0.3)
    draw_heart(160)
    time.sleep(0.3)

# Hold the final heart on screen
draw_heart(180)
heart.hideturtle()
turtle.done()