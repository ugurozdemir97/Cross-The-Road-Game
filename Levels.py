from turtle import Turtle


class Levels(Turtle):
    def __init__(self):
        super(Levels, self).__init__()
        self.hideturtle()
        self.penup()
        self.pensize(2)
        self.speed(0)

        self.levels = 1
        self.live = 5

        self.car_count = 30
        self.time_speed = 100

        self.lines()
        self.score()

    # ---------- DRAW THE BEGINNING AND ENDING LINES ----------- #

    def lines(self):
        self.goto(-300, 270)
        self.pd()
        self.seth(0)
        self.forward(650)
        self.pu()

        self.goto(-300, -270)
        self.pd()
        self.seth(0)
        self.forward(650)
        self.pu()

    # ------------------ SCOREBOARD AND LEVELS ----------------- #

    def score(self):

        # ------ Clear the existing text and write ------ #
        self.clear()
        self.goto(-280, 270)
        if self.levels < 10:
            self.write(f"Level: {self.levels} ", False, align="left", font=('Courier', 15, 'bold'))
        else:
            self.write(f"Level: MAX ", False, align="left", font=('Courier', 15, 'bold'))

        self.goto(180, 270)
        self.write(f"Lives: {self.live}", False, align="left", font=('Courier', 15, 'bold'))

    # ------------------------ GAME OVER ------------------------ #

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Courier', 40, 'bold'))
        self.clear()

    # --------------------- CONGRATULATIONS! -------------------- #

    def congrats(self):
        self.goto(0, 0)
        self.write("CONGRATULATIONS!\nYou Beat The Game", False, align="center", font=('Courier', 30, 'bold'))
        self.clear()
