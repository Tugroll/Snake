from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.highest = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        with open("highest.txt", mode="r") as file:
           high = file.read()
           self.highest = int(high)

        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}    Highest Score: {self.highest}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def check_highest(self):
        if self.score >= self.highest:
            self.highest = self.score
            with open("highest.txt", mode="w") as file:
                file.write(f"{self.highest}")
            self.clear()
            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
