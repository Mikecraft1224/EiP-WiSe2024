from jguvc_eip import basic_io
from jguvc_eip.colors import *
import time
import math

phimax = math.pi / 2
o = 1

def calc_fi(h, alpha):
    alpha = alpha + math.pi / 2
    f = math.cos(alpha) * h
    i = math.sin(alpha) * h

    return int(f), int(i)

def draw_pendulum(alpha, pendulum_center, h):
    f, i = calc_fi(h, alpha)

    basic_io.draw_line(*pendulum_center, pendulum_center[0] + f, pendulum_center[1] + i)
    basic_io.draw_circle(pendulum_center[0] + f, pendulum_center[1] + i, 10, fill_color=None)

if __name__ == '__main__':
    basic_io.start()

    t = 0

    while True:
        basic_io.clear_image()

        draw_pendulum(phimax * math.cos(o * t), (320, 240), 200)

        t += 0.016
        time.sleep(0.016)

    basic_io.wait_close()