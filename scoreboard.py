from turtle import Turtle
import time

ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):                 # ← FIXED
        super().__init__()              # ← FIXED
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 100               # +100 each food
        self.update_score()

    def reset(self):
        self.score = 0
        self.update_score()

    def game_over(self):
        self.clear()

        # Show Final Score at top
        self.goto(0, 260)
        self.color("gold")
        self.write(f"Final Score: {self.score}", align="center", font=("Courier", 24, "bold"))

        # Animated "GAME OVER"
        for size in range(10, 40, 2):
            self.clear()

            # Draw final score again
            self.goto(0, 260)
            self.color("gold")
            self.write(f"Final Score: {self.score}", align="center", font=("Courier", 24, "bold"))

            # Draw animated game over text
            self.goto(0, 0)
            self.color("red")
            self.write("GAME OVER", align="center", font=("Courier", size, "bold"))

            time.sleep(0.03)
