from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super(Paddle, self).__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.fillcolor("white")
        self.setposition(position)
        self.resizemode()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.speed("fastest")

    def up(self):
        new_y= self.ycor()+20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor()-20
        self.goto(self.xcor(), new_y)
