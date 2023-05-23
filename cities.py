from turtle import Turtle


class Cities(Turtle):

    def __init__(self, name, x, y):
        super().__init__()
        self.name = name
        self.x = x
        self.y = y
