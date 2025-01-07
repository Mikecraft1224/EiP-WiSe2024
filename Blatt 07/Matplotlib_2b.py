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
            (offset + i * binWidth, math.ceil(400 - bin * 0.6)),
            (offset + (i + 1) * binWidth, math.ceil(400 - bin * 0.6)),
            (offset + (i + 1) * binWidth, 400)
        ], fill_color=BLUE)

    basic_io.wait_close()