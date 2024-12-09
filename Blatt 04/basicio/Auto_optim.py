from jguvc_eip import basic_io
from jguvc_eip.colors import *
import time

def draw_car(x, y):
    basic_io.draw_rectangle(x, y, 150, 50, fill_color=RED)
    basic_io.draw_circle(x + 25, y + 50, 25, fill_color=BLACK)
    basic_io.draw_circle(x + 125, y + 50, 25, fill_color=BLACK)

def draw_house(x, y):
    basic_io.draw_rectangle(x, y, 150, 150, fill_color=BLUE)
    basic_io.draw_polygon([(x, y), (x + 75, y - 75), (x + 150, y)], fill_color=BLUE)

if __name__ == "__main__":
    basic_io.start()

    car_x = 0
    car_y = 375
    house_x = 350
    house_y = 300
    front = True

    z = True

    while True:
        # Double buffering
        basic_io.set_active_image(z)
        basic_io.set_visible_image(not z)

        basic_io.clear_image()

        if front:
            draw_house(house_x, house_y)
            draw_car(car_x, car_y)
        else:
            draw_car(car_x, car_y)
            draw_house(house_x, house_y)

        car_x += 1
        if car_x > 640:
            car_x = -150
            front = not front

        z = not z
        time.sleep(0.016)

    basic_io.wait_close()