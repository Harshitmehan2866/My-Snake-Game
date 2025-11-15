from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):                 # ← FIXED
        super().__init__()              # ← FIXED
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_wid=0.7, stretch_len=0.7)
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

