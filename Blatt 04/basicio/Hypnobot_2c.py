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

def draw_concentric_circle(t, circle_center):
    for r, color in zip([100, 80, 60, 40, 20], [BLUE, GREEN, YELLOW, ORANGE, RED]):
        basic_io.draw_circle(*circle_center, (r - int(t*60))%101, fill_color=None, border_color=color)

def draw_pendulum(alpha, pendulum_center, h, t):
    f, i = calc_fi(h, alpha)

    basic_io.draw_line(*pendulum_center, pendulum_center[0] + f, pendulum_center[1] + i)
    draw_concentric_circle(t, (pendulum_center[0] + f, pendulum_center[1] + i))

if __name__ == '__main__':
    basic_io.start()

    t = 0
    z = True

    while True:
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)

        basic_io.clear_image()

        draw_pendulum(phimax * math.cos(o * t), (320, 240), 150, t)

        t += 0.016

        z = not z
        time.sleep(0.016)

    basic_io.wait_close()