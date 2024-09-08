from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__() #super() is used to call the parent class
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.increase_speed()

    def bounce_x(self):
        self.x_move *= -1
        self.increase_speed()

    def reset_position(self):
        self.goto(0,0)
        self.x_move = 10  # Reset to initial x speed
        self.y_move = 10  # Reset to initial y speed
        self.move_speed = 0.1  # Reset speed

    def increase_speed(self):
        self.x_move *= 1.1
        self.y_move *= 1.1
