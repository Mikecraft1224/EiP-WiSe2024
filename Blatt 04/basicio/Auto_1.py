from jguvc_eip import basic_io
from jguvc_eip.colors import *    

if __name__ == "__main__":
    basic_io.start()

    basic_io.draw_rectangle(0, 375, 150, 50, fill_color=RED)
    basic_io.draw_circle(25, 425, 25, fill_color=BLACK)
    basic_io.draw_circle(125, 425, 25, fill_color=BLACK)

    basic_io.wait_close()