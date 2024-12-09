from jguvc_eip import basic_io
from jguvc_eip.colors import *

if __name__ == '__main__':
    basic_io.start()

    basic_io.draw_rectangle(270, 190, 100, 100)
    basic_io.draw_polygon([(320, 90), (370, 190), (320, 190)], fill_color=RED)
    basic_io.draw_polygon([(170, 240), (270, 190), (270, 240)], fill_color=BLUE)
    basic_io.draw_polygon([(320, 390), (270, 290), (320, 290)], fill_color=YELLOW)
    basic_io.draw_polygon([(470, 240), (370, 290), (370, 240)], fill_color=GREEN)

    basic_io.wait_close()