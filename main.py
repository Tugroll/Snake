from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Games")
screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = ScoreBoard()

screen.listen()
screen.onkey(my_snake.up, "Up")
screen.onkey(my_snake.down, "Down")
screen.onkey(my_snake.left, "Left")
screen.onkey(my_snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)

    my_snake.move()
    my_scoreboard.check_highest()
    if my_snake.segments[0].distance(my_food) < 15:
        my_food.refresh()
        my_snake.extend()
        my_scoreboard.increase_score()

    if (my_snake.segments[0].xcor() > 280 or my_snake.segments[0].xcor() < -280 or my_snake.segments[0].ycor() >
            280 or my_snake.segments[0].ycor() < -280):
        game_is_on = False
        my_scoreboard.game_over()


    for seg in my_snake.segments[1:]:

        if my_snake.segments[0].distance(seg) < 10:
            game_is_on = False
            my_scoreboard.game_over()


screen.exitonclick()

