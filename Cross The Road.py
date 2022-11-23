from turtle import Turtle, Screen
from Cars import Cars
from Levels import Levels
import time


# In turtle module the way to refresh screen clears everything, even the screen color. So after the screen setup,
# I will write everything in the game function. Everytime you pass a level they will be recreated.

# ------------------------------------------------- GAME -------------------------------------------------------- #

def game():  # This is the game function that will call itself again and again
    global GAME, cars, turtle

    # ---------------------------- REFRESH SCREEN ----------------------------- #

    if not GAME:
        # --------------- SCREEN COLOR AND KEY BIND ------------ #

        screen.clear()
        screen.tracer(0)  # Stop animation

        screen.colormode(255)
        screen.bgcolor((190, 190, 200))
        screen.listen()

        # --------------------- DRAW LINES ----------------------- #

        level.score()
        level.lines()

        # ----------------------- OBJECTS ----------------------- #

        cars = Cars()
        turtle = Turtle()

        # --------------------- OUR TURTLE ----------------------- #

        turtle.shape("turtle")
        turtle.shapesize(0.7, 0.7)
        turtle.seth(90)
        turtle.color("black", (75, 150, 0))
        turtle.pu()
        turtle.goto(0, -280)

        # ---------------------- BIND KEY ----------------------- #

        def up():
            turtle.forward(10)

        screen.onkey(up, "Up")

        # -------------------- CREATE CARS ---------------------- #

        for i in range(level.car_count):
            cars.create_cars()

        for i in range(200):
            cars.move()
        GAME = True

    # -------------------------------- GAME IS ON ----------------------------------- #

    screen.update()  # Update animations
    cars.move()

    # ------------------- CAR CRUSHES ------------------- #

    for car in cars.all_cars:

        if car.ycor() > turtle.ycor():  # For the cars in front of us
            if turtle.distance(car) < 16:
                level.live -= 1
                GAME = False

        elif car.ycor() < turtle.ycor():  # For the cars behind us
            if turtle.distance(car) < 14:
                level.live -= 1
                GAME = False

    # ------------------- GAME OVER ------------------- #

    if level.live == 0:
        level.score()
        level.game_over()  # Game Over feedback
        time.sleep(2)

        level.levels = 1  # Reset everything
        level.live = 5
        level.time_speed = 100
        level.car_count = 30
        GAME = False

    # ------------------- LEVEL UP -------------------- #

    if turtle.ycor() == 270:
        level.levels += 1

        if level.levels == 11:  # Congratulations feedback if beat max. level
            level.congrats()
            time.sleep(2)

        if level.levels <= 10:  # If level is less than 10 change cars speed and count
            level.time_speed -= 10
            level.car_count += 2

        else:  # After level max they will stay the same
            level.time_speed = 10
            level.car_count = 50

        level.score()
        GAME = False

    screen.ontimer(game, level.time_speed)  # When you level up, level.time_speed will be reduced 10 seconds.


# -------------------- SCREEN SETUP --------------------- #

screen = Screen()
screen.setup(600, 600)
screen.title("Cross The Road")

GAME = False

# ----------- OBJECTS ------------ #

level = Levels()  # This should be outside
cars = ""
turtle = ""

# ---------------------- START GAME --------------------- #

game()
screen.mainloop()
