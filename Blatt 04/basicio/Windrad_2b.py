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

def draw_rot_triangle(angle, tri_center, color):
    tri = [
        (tri_center[0] - 25, tri_center[1] - 50),
        (tri_center[0] + 25, tri_center[1] + 50),
        (tri_center[0] - 25, tri_center[1] + 50)
    ]

    for i in range(len(tri)):
        tri[i] = rotate_point(tri[i], angle)

    basic_io.draw_polygon(tri, fill_color=color)


if __name__ == '__main__':
    basic_io.start()

    angle = 0
    z = True

    while True:
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)

        basic_io.clear_image()

        draw_rot_rectangle(angle)
        draw_rot_triangle(angle, (345, 140), RED)
        draw_rot_triangle(angle + math.pi/2, (345, 140), GREEN)
        draw_rot_triangle(angle + math.pi, (345, 140), YELLOW)
        draw_rot_triangle(angle + 3*math.pi/2, (345, 140), BLUE)

        # For better visibility a red dot is drawn at the center of the image
        basic_io.draw_circle(*center, 5, fill_color=RED)

        angle += 0.05

        z = not z
        time.sleep(0.016)

    basic_io.wait_close()