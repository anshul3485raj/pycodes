# Simple Jardians in Python 3 for beginners
# by Ayush Negi
# scripted on 08/02/2020

# importing turtle module
import turtle

wn = turtle.Screen()
wn.title("Jardians by AYUSH_NEGI")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# score
score_a = 0 

# Paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape('square')
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=6)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('blue')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3


# Pen 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0", align="center", font=("Courier", 24, "normal"))

# functioning the paddle
def paddle_x1():
    x = paddle.xcor()
    x += 100
    paddle.setx(x)

def paddle_x2():
    x = paddle.xcor()
    x -= 100
    paddle.setx(x)




# keyboard bindings
wn.listen()

# movements
wn.onkeypress(paddle_x1, "Right")
wn.onkeypress(paddle_x2, "Left")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking for the ball
     # Border checking for ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        

     # Paddles and ball collision
    if (ball.ycor() > 240 and ball.ycor() < 250) and (ball.ycor() < paddle.ycor() + 40 and ball.ycor() > paddle.ycor() - 40):
        ball.setx(240)
        ball.dx *= -1
                