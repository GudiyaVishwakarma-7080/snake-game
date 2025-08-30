import turtle
import time
import random
import winsound   # sound ke liye

delay = 0.12
score = 0
high_score = 0

# set up the screen
wn = turtle.Screen()
wn.title("Snake Game by @Gudiya")
wn.bgcolor("green")
wn.setup(width=800, height=800)
wn.tracer(0)

# Playable area background
border = turtle.Turtle()
border.speed(0)
border.color("lightyellow")
border.penup()
border.goto(-300, -300)
border.pendown()
border.begin_fill()
for _ in range(4):
    border.forward(600)
    border.left(90)
border.end_fill()
border.hideturtle()

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 360)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    if head.direction == "down":
        head.sety(head.ycor() - 20)
    if head.direction == "left":
        head.setx(head.xcor() - 20)
    if head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop
while True:
    wn.update()

    # Border collision
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        # ⚡ border touch hone par sound
        winsound.PlaySound("crash.wav", winsound.SND_ASYNC)

        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.12
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # Food collision
    if head.distance(food) < 20:
        # ⚡ food khane par sound
        winsound.PlaySound("snake.wav", winsound.SND_ASYNC)

        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{} High Score:{}".format(score, high_score),
                  align="center", font=("Courier", 24, "normal"))

    # Move segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Body collision
    for segment in segments:
        if segment.distance(head) < 20:
            # ⚡ body touch hone par bhi crash sound
            winsound.PlaySound("crash.wav", winsound.SND_ASYNC)

            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.12

    time.sleep(delay)

wn.mainloop()
