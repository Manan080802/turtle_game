import turtle
from turtle import Turtle,Screen
import  random
screen = Screen()
is_race_on = False
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="which turtle will win race? Enter the a color: ")

colors=["red","orange","yellow","green","blue","purple"]
y_positions =[-70,-40,-10,20,50,80]
all_turtles = []
for i in range(0,6):
    tm = Turtle(shape="turtle")
    tm.shape("turtle")
    tm.color(colors[i])
    tm.penup()
    tm.goto(-250,y_positions[i])
    all_turtles.append(tm)
print(user_bet)
if user_bet:
    is_race_on=True
while is_race_on:
    if turtle.xcor()>230:
        is_race_on=False
        winning_color = turtle.pencolor()
        if winning_color==user_bet:
            print(f"You've won! the {winning_color} turtle is the winner! ")
        else:
            print(f"You've lose! the {winning_color} turtle is the winner! ")
        # print(turtle.color())
    for turtle in all_turtles:
        random_distance =random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()