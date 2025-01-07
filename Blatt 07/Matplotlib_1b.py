from jguvc_eip import basic_io
from jguvc_eip.colors import *
import numpy as np

if __name__ == '__main__':
    basic_io.start()

    table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
    tx = table[:, 6][::-1]
    offset = (640 - len(tx)) // 2

    for i in range(0, len(tx) - 1):
        basic_io.draw_line(offset + i, int(280 - tx[i]), offset + i + 1, int(280 - tx[i+1]), color=RED)

    basic_io.wait_close()