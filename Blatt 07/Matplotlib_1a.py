from jguvc_eip import basic_io
from jguvc_eip.colors import *
import numpy as np

if __name__ == '__main__':
    basic_io.start()

    table = np.loadtxt("Blatt 07\muenchen_flughafen.txt")
    # Umgedreht, da bei den Werten der neuste zuerst steht
    rr = table[:, -2][::-1]
    offset = (640 - len(rr)) // 2

    for i in range(0, len(rr)):
        basic_io.draw_circle(offset + i, int(300 - rr[i]), 2)

    basic_io.wait_close()