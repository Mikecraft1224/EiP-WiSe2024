from jguvc_eip import basic_io
from jguvc_eip.colors import *
import numpy as np
import math

if __name__ == '__main__':
    basic_io.start()

    offset = 60
    binWidth = (640 - 2 * offset) // 5

    table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
    rr = table[:, -2][::-1]
    
    minimum, maximum = np.min(rr), np.max(rr)
    binValues = np.linspace(minimum, maximum, 6)
    binValues[-1] = maximum + 1

    bins = np.zeros(5)

    for i, bin in enumerate(binValues[:-1]):
        bins[i] = np.sum(np.logical_and(rr >= bin, rr < binValues[i + 1]))
    
    for i, bin in enumerate(bins):
        basic_io.draw_polygon([
            (offset + i * binWidth, 400),
            (offset + i * binWidth, math.ceil(400 - bin * 0.75)),
            (offset + (i + 1) * binWidth, math.ceil(400 - bin * 0.75)),
            (offset + (i + 1) * binWidth, 400)
        ], fill_color=BLUE)
    
    # Axen
    basic_io.draw_line(offset - 5, 405, offset + binWidth*5 + 5, 405, color=BLACK)
    basic_io.draw_text(offset + binWidth*5 + 10, 390, "Nieder-", font_height=10)
    basic_io.draw_text(offset + binWidth*5 + 10, 400, "schlag", font_height=10)

    for i, bin in enumerate(binValues[1:-1]):
        s = str(round(bin, 2))

        basic_io.draw_line(offset + (i + 1) * binWidth, 410, offset + (i + 1) * binWidth, 400, color=BLACK)
        basic_io.draw_text(offset + (i + 1) * binWidth - 15, 410, (5-len(s)) * ' ' + str(round(bin, 2)), font_height=10)

    basic_io.draw_line(offset - 5, 405, offset - 5, 395 - math.ceil(np.max(bins) * 0.75), color=BLACK)
    basic_io.draw_text(offset - 20, 385 - math.ceil(np.max(bins) * 0.75), "Anzahl", font_height=10)

    for value in range(30, int(np.max(bins)), 30):
        i = math.ceil(value*0.75)

        basic_io.draw_line(offset - 10, 400 - i, offset, 400 - i, color=BLACK)
        basic_io.draw_text(offset - 30, 395 - i, (3 - len(str(value))) * ' ' + str(value), font_height=10)

    basic_io.wait_close()