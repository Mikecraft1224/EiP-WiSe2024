from jguvc_eip import basic_io
from jguvc_eip.colors import *
import time

def draw_concentric_circle(t, circle_center):
    for r, color in zip([100, 80, 60, 40, 20], [BLUE, GREEN, YELLOW, ORANGE, RED]):
        basic_io.draw_circle(*circle_center, (r - t)%101, fill_color=None, border_color=color)
        # Äquivalent zu:
        # basic_io.draw_circle(circle_center[0], circle_center[1], (r - t)%101, fill_color=None, border_color=color)

if __name__ == '__main__':
    basic_io.start()

    t = 0

    while True:
        basic_io.clear_image()

        draw_concentric_circle(t, (320, 240))

        t += 1
        time.sleep(0.016)

    basic_io.wait_close()