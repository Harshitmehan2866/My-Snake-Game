from turtle import Turtle

class GameOverPrompt:
    def __init__(self, screen):     # ← FIXED
        self.screen = screen
        self.active = False         # Track if prompt is active

    def play_again(self, restart_callback):
        if self.active:
            return
        self.active = True

        # Display prompt text
        self.prompt = Turtle()
        self.prompt.hideturtle()
        self.prompt.color("gold")
        self.prompt.penup()
        self.prompt.goto(0, -40)
        self.prompt.write("Play Again?", align="center",
                          font=("Courier", 24, "bold"))

        # YES Button
        self.yes = Turtle()
        self.yes.hideturtle()
        self.yes.color("lightgreen")
        self.yes.penup()
        self.yes.goto(-60, -90)
        self.yes.write("YES", align="center",
                       font=("Courier", 22, "bold"))

        # NO Button
        self.no = Turtle()
        self.no.hideturtle()
        self.no.color("red")
        self.no.penup()
        self.no.goto(60, -90)
        self.no.write("NO", align="center",
                      font=("Courier", 22, "bold"))

        # Activate click detection
        self.screen.onscreenclick(lambda x, y: self.handle_click(x, y, restart_callback))
        self.screen.update()

    def handle_click(self, x, y, restart_callback):
        # YES region
        if -100 < x < -20 and -110 < y < -70:
            self.clear_prompt()
            restart_callback()

        # NO region
        elif 20 < x < 100 and -110 < y < -70:
            self.screen.bye()

    def clear_prompt(self):
        self.prompt.clear()
        self.yes.clear()
        self.no.clear()
        self.screen.onscreenclick(None)  # Remove old click listeners
        self.active = False

