from fractal import Fractal


class Snowflake(Fractal):
    rules = {"F": "F+F--F+F"}
    angle = 60
    axiom = "F--F--F"

    top = 7


class QuadraticKochIsland(Fractal):
    axiom = "F+F+F+F"
    rules = {"F": "F-F+F+FFF-F-F+F"}
    angle = 90

    top = 4


class Crystal(Fractal):
    axiom = "F+F+F+F"
    rules = {"F": "FF+F++F+F"}
    top = 6
    angle = 90


class Carpet(Fractal):
    axiom = "YF"
    rules = {"X": "YF+XF+Y", "Y": "XF-YF-X"}
    top = 10
    angle = 60


class Square(Fractal):
    axiom = "F+F+F+F"
    rules = {"F": "FF+F+F+F+FF"}
    top = 5
    angle = 90


class Rings(Fractal):
    axiom = "F+F+F+F"
    rules = {"F": "FF+F+F+F+F+F-F"}
    top = 4
    angle = 90


class SiepinskiSieve(Fractal):
    axiom = "FXF--FF--FF"
    rules = {"F": "FF", "X": "--FXF++FXF++FXF--"}
    top = 8
    angle = 60


class ThreeDragonCurve(Fractal):
    axiom = "FX+FX+FX"
    rules = {"X": "X+YF+", "Y": "-FX-Y"}
    top = 15
    angle = 90


class Terdragon(Fractal):
    axiom = "F"
    rules = {"F": "F-F+F"}
    top = 10
    angle = 120
