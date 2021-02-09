import time
import turtle
import random
import tkinter

from picture import Picture


class Painter:
    colors = [
        "yellow",
        "gold",
        "orange",
        "red",
        "maroon",
        "violet",
        "magenta",
        "purple",
        "navy",
        "blue",
        "skyblue",
        "cyan",
        "turquoise",
        "lightgreen",
        "green",
        "darkgreen",
        "chocolate",
        "brown",
        "gray",
    ]

    def __init__(self):
        t = turtle.Turtle()

        self.wn = turtle.Screen()

        self.wn.bgcolor("black")
        self.wn.screensize(15000, 15000)
        self.wn.setup(1.0, 1.0)

        t.pensize(5)
        t.up()
        t.goto(0, 0)
        t.down()
        t.speed('fastest')

        self.t = t

    def get_random_color(self):
        return random.choice(self.colors)

    def draw(self, picture: Picture):
        self.wn.title(picture.title)

        for move in picture.algorithm:
            self.t.color(self.get_random_color())
            if move == "F":
                self.t.forward(picture.distance)
            elif move == "-":
                self.t.left(picture.angle)
            elif move == "+":
                self.t.right(picture.angle)

        turtle.done()
        turtle.mainloop()
