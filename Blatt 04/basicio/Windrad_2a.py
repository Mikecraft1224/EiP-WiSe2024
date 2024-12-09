from jguvc_eip import basic_io
from jguvc_eip.colors import *
import math
import time

center = (320, 240)

def rotate_point(point, angle):
    xr = (point[0] - center[0]) * math.cos(angle) - (point[1] - center[1]) * math.sin(angle) + center[0]
    yr = (point[0] - center[0]) * math.sin(angle) + (point[1] - center[1]) * math.cos(angle) + center[1]

    return (int(xr), int(yr))

def draw_rot_rectangle(angle):
    rect = [
        (270, 190),
        (370, 190),
        (370, 290),
        (270, 290)
    ]

    for i in range(len(rect)):
        rect[i] = rotate_point(rect[i], angle)

    basic_io.draw_polygon(rect)

if __name__ == '__main__':
    basic_io.start()

    angle = 0
    while True:
        basic_io.clear_image()

        draw_rot_rectangle(angle)

        # For better visibility a red dot is drawn at the center of the image
        basic_io.draw_circle(*center, 5, fill_color=RED)

        angle += 0.05

        time.sleep(0.016)

    basic_io.wait_close()