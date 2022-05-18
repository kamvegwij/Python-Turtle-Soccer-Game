import turtle
import winsound

wn = turtle.Screen()
wn.title('Soccer by Gwij')
wn.bgcolor('black')
wn.setup(width=800,  height=600)
wn.tracer(0)


# Draw the borders
border = turtle.Turtle()
border.pensize(3)
border.color('green')

border.penup()
border.goto(-380, 305)
border.pendown()
border.begin_fill()
border.setheading(0)
border.forward(770)
border.setheading(270)
border.forward(601)
border.setheading(180)
border.forward(760)
border.setheading(90)
border.forward(601)
border.end_fill()

# Make soccer poles

pole_one = turtle.Turtle()
pole_one.color('white')
pole_one.penup()
pole_one.goto(-380, 100)
pole_one.pendown()
pole_one.pensize(2)
pole_one.setheading(0)
pole_one.forward(120)
pole_one.setheading(270)
pole_one.forward(180)
pole_one.setheading(180)
pole_one.forward(120)

pole_two = turtle.Turtle()
pole_two.color('white')
pole_two.penup()
pole_two.goto(380, 100)
pole_two.pendown()
pole_two.pensize(2)
pole_two.setheading(180)
pole_two.forward(120)
pole_two.setheading(270)
pole_two.forward(180)
pole_two.setheading(0)
pole_two.forward(130)

# Graphics for the soccer pitch

line = turtle.Turtle()
line.color('white')
line.pensize(2)
line.setheading(90)
line.forward(300)
line.setheading(270)
line.forward(601)

wn = turtle.Screen()
wn.title('Pong by Gwij')
wn.bgcolor('black')
wn.setup(width=800,  height=600)
wn.tracer(0)

# Paddle A

paddle_A = turtle.Turtle()
paddle_A.speed(0)
paddle_A.shape('square')
paddle_A.color('white')
paddle_A.shapesize(stretch_wid=3, stretch_len=1)

paddle_A.penup()
paddle_A.goto(-350, 0)


# Paddle Bpaddle_A = turtle.Turtle()
paddle_B = turtle.Turtle()
paddle_B.speed(0)
paddle_B.shape('square')
paddle_B.color('white')
paddle_B.shapesize(stretch_wid=3, stretch_len=1)

paddle_B.penup()
paddle_B.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')

ball.penup()
ball.goto(0, 0)

# Ball Speed
ball.dx = 1.2
ball.dy = 1.2

# Fucntions to move paddles
def paddle_A_up():
    y = paddle_A.ycor()
    y += 20
    paddle_A.sety(y)

def paddle_A_down():
    y = paddle_A.ycor()
    y -= 20
    paddle_A.sety(y)

def paddle_B_up():
    y = paddle_B.ycor()
    y += 20
    paddle_B.sety(y)

def paddle_B_down():
    y = paddle_B.ycor()
    y -= 20
    paddle_B.sety(y)

# Keyboard binding
wn.listen()
wn.onkey(paddle_A_up, 'w')
wn.onkey(paddle_A_down, 'z')
wn.onkey(paddle_B_up, 'Up')
wn.onkey(paddle_B_down, 'Down')


# Pen to draw score

pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,270)
pen.write('Player A : 0    Player B: 0', align='center', font=('Arial', 22, 'bold'))

# Track score

score_A = 0
score_B = 0

# Main game loop

while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)


    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    # Scoring when out of bounds
    
    if ball.xcor() > 390 and ball.ycor() > 100:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))
        
    if ball.xcor() < -390 and ball.ycor() > 100:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))

    if ball.xcor() > 390 and ball.ycor() < -100:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))
        
    if ball.xcor() < -390 and ball.ycor() < -100:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))
        
        # Paddle v Ball collision
    # Ball bounces of the paddle:
    if ball.xcor() > 340 and (ball.xcor() < 350) and (ball.ycor() < paddle_B.ycor() + 50 and ball.ycor() > paddle_B.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1


    if ball.xcor() < -340 and (ball.xcor() < -350) and (ball.ycor() < paddle_A.ycor() + 50 and ball.ycor() > paddle_A.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        
    # Score through poles

    if (ball.ycor() < 100) and (ball.ycor() > -100) and (ball.xcor() > -388)  and (ball.xcor() <= -390):
        score_A += 2
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))
        
    if (ball.ycor() < 100) and (ball.ycor() > -100) and (ball.xcor() <= 390)  and (ball.xcor() >= 388):
        score_B += 2
        pen.clear()
        pen.write('Player A : {0}    Player B: {1}'.format(score_A, score_B), align='center', font=('Arial', 22, 'bold'))

