from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("blue")
        self.speed("fastest")
        rnd_x = random.randint(-280,280)
        rnd_y = random.randint(-280,280)
        self.goto(rnd_x,rnd_y)

    def refresh(self):
        rnd_x = random.randint(-280, 280)
        rnd_y = random.randint(-280, 280)
        self.goto(rnd_x, rnd_y)



