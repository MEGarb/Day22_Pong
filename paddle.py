from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        """side must be 'left' or 'right'"""
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1.0, stretch_wid=5.0)
        self.speed("fastest")
        if side == 'right':
            self.x_pos = 350
        elif side == 'left':
            self.x_pos = -350

        self.goto(self.x_pos, 0)
        self.showturtle()

    def move_up(self):
        self.goto(self.x_pos, self.ycor() + 20)

    def move_down(self):
        self.goto(self.x_pos, self.ycor() + -20)

    def reset(self):
        self.goto(self.x_pos, 0)
