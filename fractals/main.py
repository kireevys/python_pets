from painter import Painter
from all_fractals import *

if __name__ == "__main__":
    picture = Terdragon(7).build_picture(50)
    Painter().draw(picture)
