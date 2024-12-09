from jguvc_eip import basic_io
from jguvc_eip.colors import *

if __name__ == "__main__":
    basic_io.start()

    basic_io.draw_rectangle(350, 300, 150, 150, fill_color=BLUE)
    basic_io.draw_polygon([(350, 300), (425, 225), (500, 300)], fill_color=BLUE)

    basic_io.wait_close()