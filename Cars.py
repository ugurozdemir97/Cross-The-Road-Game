from turtle import Turtle
from random import choice, randint


# ---------------- Possible colors and positions of cars --------------- #

COLORS = ["red", "yellow", "blue", "purple", "orange", "green", "gold", "tomato", "VioletRed", "salmon", "turquoise",
          "RoyalBlue", "SeaGreen", "OrangeRed", "magenta", "aquamarine", "cyan", "DarkGreen"]
YCOR = [-245, -205, -165, -125, -85, -45, 245, 205, 165, 125, 85, 45, 0]


class Cars(Turtle):
    def __init__(self):
        super(Cars, self).__init__()
        self.hideturtle()

        self.all_cars = []  # This list will hold all car objects

        self.create_cars()

    # --------------------- CREATE CARS ------------------- #

    def create_cars(self):

        # ---- CREATE ONE CAR --- #

        new_car = Turtle()
        new_car.penup()
        new_car.color("black", choice(COLORS))
        new_car.shape("square")
        new_car.shapesize(1, 2)
        new_car.seth(180)

        # --- PLACE IT ON A Y AXIS FROM YCOR --- #

        def place():
            new_car.goto(randint(310, 910), choice(YCOR))

            for cars in self.all_cars:
                if new_car.distance(cars) < 45:
                    place()
                    # Unless the new car is not on top of others this function will call itself.
                    # When it's not on any car function loop will end.

        place()

        self.all_cars.append(new_car)

    # ---------------------- MOVE CARS --------------------- #

    def move(self):

        # In turtle module you can't delete the turtle objects entirely. Even though you delete them they still
        # use memory, so if there are a lot of cars and move forever, at one point it starts to use GPU too much.

        # So I decided to create cars and use the same cars by turning them from the end to the beginning
        # outside the window.

        for i in self.all_cars:  # Move cars in a rectangle
            if i.xcor() < -310:
                i.right(90)
                i.forward(620)
                i.right(90)
                i.forward(620)
                i.right(90)
                i.forward(620)
                i.right(90)
            i.forward(5)





