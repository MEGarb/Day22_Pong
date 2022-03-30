from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.penup()
        self.shape("circle")
        self.goto(0, 0)
        self.x_vec = 10
        self.y_vec = 10
        self.move_speed = 0.1

    def move(self):
        self.goto(self.xcor() + self.x_vec, self.ycor() + self.y_vec)

    def bounce(self):
        self.y_vec *= -1

    def paddle_hit(self):
        self.x_vec *= -1
        self.move_speed *= .9

    def reset_pos(self, dir):
        self.goto(0, 0)
        self.move_speed = .1
        if dir == 'left':
            self.x_vec = 10
            self.y_vec = 10
        elif dir == 'right':
            self.x_vec = -10
            self.y_vec = 10
