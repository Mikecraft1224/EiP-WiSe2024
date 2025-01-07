from jguvc_eip import basic_io
from jguvc_eip.colors import *
import numpy as np

if __name__ == '__main__':
    basic_io.start()

    table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
    rr = table[:, -2][::-1]
    tx = table[:, 6][::-1]
    offset = (640 - len(rr)) // 2

    for i in range(0, len(tx) - 1):
        basic_io.draw_line(offset + i, int(280 - tx[i]), offset + i + 1, int(280 - tx[i+1]), color=RED)

    for i in range(0, len(rr)):
        basic_io.draw_circle(offset + i, int(300 - rr[i]), 1)
    
    # Axen
    basic_io.draw_line(offset - 5, 305, offset + len(rr) + 5, 305)

    basic_io.draw_line(offset - 5, 305, offset - 5, 220)
    basic_io.draw_text(offset - 35, 200, "Temperatur", font_height=10, color=RED)

    for i in range(-10, 40, 10):
        basic_io.draw_line(offset - 8, 280 - i, offset - 2, 280 - i)
        basic_io.draw_text(offset - 30, 280 - i - 5, (3 - len(str(i))) * ' ' + str(i), font_height=10, color=RED)

    basic_io.draw_line(offset + len(rr) + 5, 305, offset + len(rr) + 5, 220)
    basic_io.draw_text(offset + len(rr) - 30, 200, "Niederschlag", font_height=10)

    for i in range(0, 50, 10):
        basic_io.draw_line(offset + len(rr) + 2, 300 - i, offset + len(rr) + 8, 300 - i)
        basic_io.draw_text(offset + len(rr) + 10, 300 - i - 5, str(i), font_height=10)


    basic_io.wait_close()