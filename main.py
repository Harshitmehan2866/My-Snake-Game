# The Snake Game by Parmeet Singh (Final Replay + Start Interface)
from turtle import Screen, Turtle
from scoreboard import Scoreboard      # ← FIXED
from snake import Snake
from food import Food
from replay import GameOverPrompt
import time

# ---------------- SETUP ----------------
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = False
snake = None
food = None
scoreboard = None
prompt = None

# ---------------- START INTERFACE ----------------

def show_start_screen():
    """Display the starting interface before the game begins."""
    screen.clear()
    screen.bgcolor("black")

    pen = Turtle()
    pen.hideturtle()
    pen.color("Green")
    pen.penup()
    pen.goto(0, 60)
    pen.write("🐍 WELCOME TO SNAKE GAME 🐍", align="center", font=("Courier", 24, "bold"))

    pen.goto(0, 0)
    pen.write("Press 'S' to Start 😉", align="center", font=("Courier", 18, "bold"))

    pen.goto(0, -40)
    pen.write("Press 'Q' to Quit ☹", align="center", font=("Courier", 18, "bold"))

    # Instructions
    pen.color("Blue")
    pen.goto(0, -80)
    pen.write("How To Play 🎮", align="center", font=("Courier", 18, "bold"))
    pen.goto(0, -120)
    pen.write(" 'W' to UP", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -140)
    pen.write(" 'S' to DOWN", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -160)
    pen.write(" 'A' to LEFT", align="center", font=("Courier", 18, "normal"))
    pen.goto(0, -180)
    pen.write(" 'D' to RIGHT", align="center", font=("Courier", 18, "normal"))

    # Credits
    pen.color("Yellow")
    pen.goto(200, -260)
    pen.write("Created by Harshit Mehan", align="center", font=("Courier", 8, "normal"))

    screen.listen()
    screen.onkey(start_game, "s")
    screen.onkey(quit_game, "q")


def quit_game():
    screen.bye()


# ---------------- GAME LOOP ----------------
def game_loop():
    global game_is_on
    if not game_is_on:
        return

    screen.update()
    time.sleep(0.07)
    snake.move()

    # Collision with food
    if snake.head.distance(food) < 15:
        food.refresh_position()
        snake.extend()
        scoreboard.increase_score()

    # Collision with wall
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        end_game()
        return

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_game()
            return

    screen.ontimer(game_loop, 70)


# ---------------- ENDING ----------------
def end_game():
    global game_is_on
    game_is_on = False
    scoreboard.game_over()
    prompt.play_again(restart_game)


# ---------------- START FUNCTION ----------------
def start_game():
    global game_is_on, snake, food, scoreboard, prompt

    screen.clear()
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    prompt = GameOverPrompt(screen)

    screen.listen()
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")

    game_is_on = True
    screen.update()
    game_loop()


# ---------------- RESTART FUNCTION ----------------
def restart_game():
    start_game()


# ---------------- START MENU ----------------
show_start_screen()
screen.mainloop()
